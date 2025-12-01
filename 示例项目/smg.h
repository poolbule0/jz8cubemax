#ifndef __SMG_H__
#define __SMG_H__
#include "type.h"
typedef struct Sys_FlagLed_Bit_
{
    unsigned char bit0 : 1;
    unsigned char bit1 : 1;
    unsigned char bit2 : 1;
    unsigned char bit3 : 1;
    unsigned char bit4 : 1;
    unsigned char bit5 : 1;
    unsigned char bit6 : 1;
    unsigned char bit7 : 1;
} Sys_FlagLed_Bit;


typedef union Sys_FlagLed_Class_
{
    unsigned char flag_all;
    Sys_FlagLed_Bit Sys_Flag;
    
}Sys_FlagLed_Class;

extern Sys_FlagLed_Class Flag_Led1;
#define B1_LED Flag_Led1.Sys_Flag.bit1
#define C1_LED Flag_Led1.Sys_Flag.bit2
#define SMG_BAI Flag_Led1.flag_all

extern Sys_FlagLed_Class Flag_Led2;
#define A2_LED Flag_Led2.Sys_Flag.bit0
#define B2_LED Flag_Led2.Sys_Flag.bit1
#define C2_LED Flag_Led2.Sys_Flag.bit2
#define D2_LED Flag_Led2.Sys_Flag.bit3
#define E2_LED Flag_Led2.Sys_Flag.bit4
#define F2_LED Flag_Led2.Sys_Flag.bit5
#define G2_LED Flag_Led2.Sys_Flag.bit6
#define SMG_SHI Flag_Led2.flag_all


extern Sys_FlagLed_Class Flag_Led3;
#define A3_LED Flag_Led3.Sys_Flag.bit0
#define B3_LED Flag_Led3.Sys_Flag.bit1
#define C3_LED Flag_Led3.Sys_Flag.bit2
#define D3_LED Flag_Led3.Sys_Flag.bit3
#define E3_LED Flag_Led3.Sys_Flag.bit4
#define F3_LED Flag_Led3.Sys_Flag.bit5
#define G3_LED Flag_Led3.Sys_Flag.bit6
#define SMG_GE Flag_Led3.flag_all

extern Sys_FlagLed_Class Flag_Led4;
#define    B_LED_LIGHTING		(Flag_Led4.Sys_Flag.bit0)
#define    B_LED_PERCENT_SIGNS	(Flag_Led4.Sys_Flag.bit1)
#define    SMG_TU                   Flag_Led4.flag_all



#define IO_LED1 	PORT5_2
#define IO_LED2	    PORT5_1
#define IO_LED3	    PORT5_0
#define IO_LED4	    PORT6_7
#define IO_LED5	    PORT6_6


#define	IO_LED1_CON	P5CON_2
#define	IO_LED2_CON	P5CON_1
#define	IO_LED3_CON	P5CON_0
#define	IO_LED4_CON	P6CON_7
#define	IO_LED5_CON	P6CON_6

#define IO_IN() {\
   IO_LED1_CON=1;\
   IO_LED2_CON=1;\
   IO_LED3_CON=1;\
   IO_LED4_CON=1;\
   IO_LED5_CON=1;\
}
#define IO_OUT_L() {\
    IO_LED1=0;\
    IO_LED2=0;\
    IO_LED3=0;\
    IO_LED4=0;\
    IO_LED5=0;\
    IO_LED1_CON=0;\
    IO_LED2_CON=0;\
    IO_LED3_CON=0;\
    IO_LED4_CON=0;\
    IO_LED5_CON=0;\
    IO_LED1=0;\
    IO_LED2=0;\
    IO_LED3=0;\
    IO_LED4=0;\
    IO_LED5=0;\
}

#define PIN1_L() {IO_LED1=0;IO_LED1_CON=0;IO_LED1=0;}
#define PIN2_L() {IO_LED2=0;IO_LED2_CON=0;IO_LED2=0;}
#define PIN3_L() {IO_LED3=0;IO_LED3_CON=0;IO_LED3=0;}
#define PIN4_L() {IO_LED4=0;IO_LED4_CON=0;IO_LED4=0;}
#define PIN5_L() {IO_LED5=0;IO_LED5_CON=0;IO_LED5=0;}

#define PIN1_H() {IO_LED1=1;IO_LED1_CON=0;IO_LED1=1;}
#define PIN2_H() {IO_LED2=1;IO_LED2_CON=0;IO_LED2=1;}
#define PIN3_H() {IO_LED3=1;IO_LED3_CON=0;IO_LED3=1;}
#define PIN4_H() {IO_LED4=1;IO_LED4_CON=0;IO_LED4=1;}
#define PIN5_H() {IO_LED5=1;IO_LED5_CON=0;IO_LED5=1;}


void SMG_Display(unsigned char a ,unsigned char b);
void SMG_Scan(void); //ÊýÂë¹ÜÉ¨Ãèº¯Êý
#endif

