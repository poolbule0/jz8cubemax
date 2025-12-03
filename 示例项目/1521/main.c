#include "main.h"

SYS_FlgBitClass	U_Flage;	
uint8_t r_g_workMod;

void main()
{
	fw_clrRam();		//清RAM
	fw_gpioInit();		//端口初始化
	fw_tc0Init();		//定时器初始化
	fw_pwm1Init();

	EI();				//开启中断
	while(1)
	{
		if (Time_10ms)
		{
			Time_10ms = DISABLE;
			fw_sleepEvent();
            keyProcess();

			
		}
	}
}
