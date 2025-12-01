#include "sleep.h"
#include "type.h"
#include "main.h"
unsigned char sleep_cnt = 0;
//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
//***************睡眠程序*****************
//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
void sleep_scan(void)
{
	if(F_CHARGE == 0 && F_CHARGE_FULL == 0 && r_g_workMod == 0)
	{
	if(++ sleep_cnt >= 5){
		sleep_cnt = 0;

		ADIS = 0;
		ADCON0 = 0;	
		ADCON1 = 0;
		PORT5 = 0x00;
		PORT6 = 0x00;
	
		TC0C = 0;
		WDTCON = 0x00;	
		INTE0=0x04;	
		
		INTF0 = 0;
		INTF1 = 0;
		di();				//禁止唤醒进入中断
		sleep();
		nop(); 
		nop();
		nop();
		nop();
		cwdt();
	//------------睡眠唤醒----------------------
		INTE0 = 0;	//
		//===========TC0初始化==============
		TC0CON = 0x82;		//TC0控制寄存器			
		TC0C = TCC_NUM;		//TC0计数寄存器
		INTE0 |= 0x01;		//中断使能 
	
		INTF0 = 0;
		INTF1 = 0;
		ei();	
		
	}

	}
	
	else{
		sleep_cnt = 0;
	}

}