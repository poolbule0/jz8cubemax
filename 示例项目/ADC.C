#include "main.h"
#include "ADC.H"

uint16_t ADC_value; 
uint16_t ADC_GetValue(uint8_t chn,uint8_t vref)
{
    uint16_t delay_time = 0;
     
    uint16_t ADC_value_high = 0;
    uint16_t ADC_value_low = 0xffff;
    uint32_t ADC_value_sum = 0;
    uint8_t count = 0;

	// //===========AD初始化===============
    // P5ADE=0X00;		//P5模拟端口控制
    // P6ADE=0X00;		//P6模拟端口控制
    
    ADIS = (chn << 4);		        //AD采样口使能口
    ADCON0 = vref | C_Ckl_Div16;	//AD基准电压及分频选择,16分频

    ADCON1 = C_ADC_START;	//AD使能，不校准

    // ADCON0 = 0x04;
    // ADCON1 = 0x40;
    // ADIS = 0XE0;

   for(count = 0; count < 10; count++)
   {
        ADRUN = 1;
        delay_time = DELAY_TIME;
        while(ADRUN && (--delay_time));

        ADC_value = ADIS & 0x0f;
        ADC_value = (ADC_value << 8) + ADATL;
        if(ADC_value > ADC_value_high)
        {
            ADC_value_high = ADC_value;
        }
        if(ADC_value < ADC_value_low)
        {
            ADC_value_low = ADC_value;
        }
        ADC_value_sum += ADC_value;
    }

    ADC_value = (ADC_value_sum - ADC_value_high - ADC_value_low + 4) >> 3;

    return ADC_value;
}

