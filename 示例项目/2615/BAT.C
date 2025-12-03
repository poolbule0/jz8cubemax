#include "BAT.h" 
/*上电检测AD值，并且延迟变化，
当充电模式的时候，进入充电模式，此时电池充电中，电压不断升高，
进入充电模式的判断，如果现在的电量值比之前的电量值高连续15次，则需要延迟变化，变化到增加到的电压值，最大为100.
当放电模式的时候，进入放电模式，此时电池放电中，电压不断降低，
进入放电模式的判断，如果现在的电量值比之前的电量值低连续15次，则需要延迟变化，变化到减少到的电压值，最小为0.
当电量低于10时会加速放电，延迟时间缩短
*/
const uint16_t t_tabBatValTab[] = {\
1499,\
1505,\
1511,\
1517,\
1523,\
1530,\
1536,\
1542,\
1548,\
1554,\
1561,\
1567,\
1573,\
1579,\
1585,\
1592,\
1598,\
1604,\
1610,\
1616,\
1623,\
1629,\
1635,\
1641,\
1647,\
1654,\
1660,\
1666,\
1672,\
1678,\
1685,\
1691,\
1697,\
1703,\
1709,\
1716,\
1722,\
1728,\
1734,\
1740,\
1747,\
1753,\
1759,\
1765,\
1771,\
1778,\
1784,\
1790,\
1796,\
1802,\
1809,\
1815,\
1821,\
1827,\
1833,\
1840,\
1846,\
1852,\
1858,\
1864,\
1871,\
1877,\
1883,\
1889,\
1895,\
1902,\
1908,\
1914,\
1920,\
1926,\
1933,\
1939,\
1945,\
1951,\
1957,\
1964,\
1970,\
1976,\
1982,\
1988,\
1995,\
2001,\
2007,\
2013,\
2019,\
2026,\
2032,\
2038,\
2044,\
2050,\
2057,\
2063,\
2069,\
2075,\
2081,\
2088,\
2094,\
2100,\
2106,\
2115,\
2119,\
};

uint8_t r_g_batVal;					//电流挡位
uint16_t r_gbatvalsum;			//电池电压累加值
uint8_t r_gbatvalcnt;			//电池电压累加次数
uint8_t r_buff;
uint16_t adcValue ;     // ADC采样值


uint8_t r_g_batValChangeCnt;    //电压挡位变化总次数
uint8_t r_g_batValAddCnt;		//电压挡位增加次数 		
uint8_t r_g_batValDecCnt;		//电压挡位减少次数

uint16_t r_g_batValAddShk;      //计时电量延时变化 充电
uint16_t r_g_batValDecShk;      //计时电量延时变化 放电
uint16_t r_g_batValChangeShkSet;   //设置延时变化时间


/***************************************************
*
* 函数 : sw_adcBatVal
* 功能 : ADC检测总电池电量
*
****************************************************/
void sw_adcBatVal(void)
{
    uint8_t left = 0;          // 查找范围左边界
    uint8_t right = 101;       // 查找范围右边界
    uint8_t median = 0;        // 中间值


    adcValue = ADC_GetValue(E_AD14, E_Vrefh_1_5V);

    
    // 二分查找
    while (1)
    {
        // 计算中间值
         median = left + right;
		 median = median >> 1;
        
        // 如果左右边界相等，查找结束
        if (left == median)
        {
            break;
        }
        
        // 比较ADC值与查表值
        if (adcValue < t_tabBatValTab[median])
        {
            right = median;    // 目标值在左半部分
        }
        else
        {
            left = median;     // 目标值在右半部分
        }
    }
    if(r_gbatvalcnt == 0)
    {
        r_gbatvalsum = 0;
    }
    
    median = 100 - median;
    r_gbatvalsum += median;

      if(++r_gbatvalcnt >= 16)
    {
        r_gbatvalcnt = 0;
        
        r_gbatvalsum += 8;
        r_gbatvalsum = r_gbatvalsum >> 4; // 平均值
        if (r_gbatvalsum > D_CHECK_BAT_VAL_NUM)
        {
            r_gbatvalsum = D_CHECK_BAT_VAL_NUM;
        }

        if(F_FIRST_POWER_UP == 1 )
        {
            F_FIRST_POWER_UP = 0;
            r_buff = r_gbatvalsum;
            r_g_batVal = r_buff;            // 返回找到的电量百分比
        }
		else if(F_CHARGE == 1 || r_g_workMod)
        {
            

            if(++r_g_batValChangeCnt <= D_BAT_VAL_CNT_SHK)
            {
                if(r_gbatvalsum > r_buff)
                {
                    r_g_batValAddCnt++;
                }
                else if(r_gbatvalsum < r_buff)
                {
                    r_g_batValDecCnt++;
                }
                
            }
            else{

                if(r_g_batValAddCnt > D_BAT_VAL_ADD_SHK && F_CHARGE == ENABLE)
                {
                    r_buff = r_gbatvalsum;
                }
                else if(r_g_batValDecCnt > D_BAT_VAL_DEC_SHK&& F_CHARGE == DISABLE && r_g_workMod)
                {
                    r_buff = r_gbatvalsum;
                }
                r_g_batValChangeCnt = 0;
                r_g_batValDecCnt = 0;
                r_g_batValAddCnt = 0;
            }
            if(F_CHARGE == ENABLE)
            {
               r_g_batValChangeShkSet = 100; //7.5s
            }
            else if(r_g_workMod)
            {
                if(r_buff < 10)
                {
                    r_g_batValChangeShkSet = 40;
                }
                else
                {
                    r_g_batValChangeShkSet = 100;
                }
            }
            if(F_CHARGE)
            {
                r_g_batValDecShk = 0; //放电计时清零
                if(F_CHARGE_FULL || r_buff > r_g_batVal)
                {
                    if(++r_g_batValAddShk >= r_g_batValChangeShkSet)
                    {
                        r_g_batValAddShk = 0;
                        if(r_g_batVal < 100)
                        {
                            r_g_batVal++;
                        }
                    }
                }
            }
            else if(r_g_workMod)
            {
                r_g_batValAddShk = 0; //充电计时清零
                if(r_buff < r_g_batVal)
                {
                    if(++r_g_batValDecShk >= r_g_batValChangeShkSet)
                    {
                        r_g_batValDecShk = 0;
                        if(r_g_batVal > 0)
                        {
                            r_g_batVal--;
                        }
                    }
                }
            }
            else
            {
                r_g_batValAddShk = 0;
                r_g_batValDecShk = 0;
            }
            if (r_g_workMod != DISABLE && r_buff == 0 && F_CHARGE == DISABLE)
            {
                r_g_workMod = 0;
                r_g_batVal = 0;

            }
        }
        

    }
	// return r_g_batVal;  // 返回找到的电量百分比
    
   
}

