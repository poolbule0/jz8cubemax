#include "JZ8P2615.h"
#include "main.h"
#include "init.h"
#include "type.h"

#include "ADC.H"
#include "BAT.H"
#include "smg.h"
#include "mode.h"

#include "sleep.h"


SYS_FlgBitClass U_Flage1;
uint8_t r_g_workMod;
uint8_t led_turn_cnt;
uint8_t led_turn;

void main(void)
{
	file_clrRam();
   	file_init();					//初始化
	file_tc0_Init();
	ei();
	F_FIRST_POWER_UP = 1;
	r_g_workMod = 0;
	F_CHARGE = 0;
	F_CHARGE_FULL = 0;
	
    while(1)
	{	 
		cwdt();				//清看门狗
		
        if(Time_10ms == 1)
        {
            Time_10ms = 0;	
			sleep_scan();

			//工作模式为放电模式
			if(r_g_workMod == 1 && F_CHARGE == 0 && F_CHARGE_FULL == 0)
			{
				SMG_Display(r_g_batVal,0x02);
				Io_Motoer = 1;

			}
			//工作模式为充电模式
			else if(r_g_workMod == 0 && F_CHARGE == 1 && F_CHARGE_FULL == 0)
			{
				if(++led_turn_cnt >= 50)
				{
					led_turn_cnt = 0;
					led_turn ^= 0x01;
				}
				SMG_Display(r_g_batVal,led_turn + 0x02);
				Io_Motoer = 0;
			}
			//工作模式为满电模式
			else if(F_CHARGE_FULL == 1)
			{
				SMG_Display(0x64,0x03);
				Io_Motoer = 0;
			}
			else
			{
				Io_Motoer = 0;	

			}
			
        }
		 if(Time_200us == 1)
        {
            Time_200us = 0;	 
			Mode_Check();
			sw_adcBatVal();
			
			
			
        }
	}
}
