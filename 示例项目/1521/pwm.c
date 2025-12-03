#include "pwm.h"


//p62
void pwm1Init()
{
    /********** 选择PWM模块时钟 *************/
    PWMCON |= 0x80;
    PWMCON |= D_PWM_DIV_SLCT;
	PWMCON |= 0x10;
	

	CPUCON = 0; //bit7:IPWM1-PWM互补输出 1：pwm取反 bit6:时钟源选择1：系统时钟0：指令时钟 bit4:PWMWE-PWM 唤醒 1:PWM 唤醒使能，可唤?芽障心Ｊ?

	PRD = 100;		//PWM周期

	PDC1 = 50;		//pwmDUTY

	IOCP_W(IMR,0X01);		//TCC中断 关闭pwm中断

	ISR = 0xf7;			//清除溢出标志位
}
void pwm2Init()
{
    /********** 选择PWM模块时钟 *************/
    PWMCON |= 0x80;
    PWMCON |= D_PWM_DIV_SLCT;
	PWMCON |= 0x20;

	CPUCON = 0; //bit7:IPWM1-PWM互补输出 1：pwm取反 bit6:时钟源选择1：系统时钟0：指令时钟 bit4:PWMWE-PWM 唤醒 1:PWM 唤醒使能，可唤?芽障心Ｊ?

	PRD = 100;		//PWM周期

	PDC2 = 50;		//pwmDUTY

	IOCP_W(IMR,0X01);		//TCC中断 关闭pwm中断

	ISR = 0xf7;			//清除溢出标志位
}

void pwm3Init()
{
    /********** 选择PWM模块时钟 *************/
    PWMCON |= 0x80;
    PWMCON |= D_PWM_DIV_SLCT;
	PWMCON |= 0x40;

	CPUCON = 0; //bit7:IPWM1-PWM互补输出 1：pwm取反 bit6:时钟源选择1：系统时钟0：指令时钟 bit4:PWMWE-PWM 唤醒 1:PWM 唤醒使能，可唤?芽障心Ｊ?

	PRD = 100;		//PWM周期

	PDC3 = 50;		//pwmDUTY

	IOCP_W(IMR,0X01);		//TCC中断 关闭pwm中断

	ISR = 0xf7;			//清除溢出标志位
}