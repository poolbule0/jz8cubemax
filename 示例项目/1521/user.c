#include "user.h"

//===================================//
//初始化RAM:10H~3FH
//===================================//
void fw_clrRam()
{
	for(RSR=0x90;RSR<0xFF;RSR++)	//清零 BANK0 RAM  IAR-R0,RSR-R4
	{IAR = 0;}
	 IAR = 0;
}

//===================================//
//端口初始??
//===================================//
void fw_gpioInit(void)
{	
	IOCP_W(P5CR,0x00);		//P5口设为输出
	PORT5 = 0;				//P5口输出低

	IOCP_W(P6CR,0x01);		//P6口设为输出
	PORT6 = 0;				//P6口输出低

	IOCP_W(PHDCR,0xff);		//端口上下拉控制寄存器，bit7-bit4对应P67-P64下拉;bit3-bit0对应P53-P50上拉 
	IOCP_W(PDCR,0xff);		//端口下拉控制寄存器，  bit6-bit4对应P62-P60,bit3-bit0对应P53-P50

	IOCP_W(PHCR,0xfe);		//P6端口上拉控制寄存?? bit7-bit0对应P67-P60

	IOCP_W(WDTCR,0x00);		//WDT 使能控制寄存??

	ICIECR=0X00;		//P63端口独立唤醒
}

//===================================//
//TC0初始化
//===================================//
void fw_tc0Init()
{
	CONTW(0X02);			//TCC 8分频

	IOCP_W(IMR,0X01);		//TCC中断

	TCC = TCC_TIM;			//1/2 * 8 * (256-6) = 1000us	鍏?寮忥拷?/IRC棰戠巼 * 棰勫垎锟??* 锟??56-鍒濆�硷級

	ISR = 0xfe;
}
