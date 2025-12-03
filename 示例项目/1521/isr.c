#include"user.h"

unsigned char reg_200us;  
unsigned char reg_10ms;
volatile __at(0x10) uint8_t A_BUFF;		//中断ACC保护RAM
volatile __at(0x11) uint8_t R3_BUFF;		//中断STATUS保护RAM


void int_isr(void) __interrupt 
{    	
	__asm__("org 0x08");			//中断入口地址	
    DI();		
	PUSH(_A_BUFF,_R3_BUFF);			//中断入栈保护
//=========Tcc中断程序===============//
	if(TCIF == 1)					//判断TCIF是否为1
	{
		TCC += TCC_TIM;			//1/2 * 8 * (256-6) = 1000us	公式：1/IRC频率 * 预分频 * （256-初值）
		ISR = 0xfe;				//清TC0中断标志位

        if (++ reg_10ms >= 1)
        {
            reg_10ms = 0;
            Time_10ms = ENABLE;
		
        }
	}	
//===============中断程序===============//
	ISR = 0x01; //清不使用的中断标志位
	POP(_A_BUFF,_R3_BUFF);			//中断出栈保护恢复
    EI();
}

