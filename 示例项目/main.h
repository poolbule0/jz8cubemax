
#ifndef __MAIN_H__
#define __MAIN_H__

#include "JZ8P2615.h"
#include "type.h"

#define	TCC_NUM	206     

#define Io_Charge	    PORT6_5
#define Io_Charge_full  PORT6_4
#define Io_Key	        PORT6_3
#define Io_Motoer       PORT6_2

typedef struct SYS_FlgBit_
{   
    uint8_t bit0:1; 
    uint8_t bit1:1;              
    uint8_t bit2:1;
    uint8_t bit3:1;
    uint8_t bit4:1;
    uint8_t bit5:1;
    uint8_t bit6:1;
    uint8_t bit7:1;
}SYS_FlgBit;
typedef union SYS_FlgBitClass_
{
    uint8_t       FlgAll;
    SYS_FlgBit    SYS_Flg;
}SYS_FlgBitClass;	

extern SYS_FlgBitClass	U_Flage1;
#define	Time_10ms		        (U_Flage1.SYS_Flg.bit0)
#define Time_200us				(U_Flage1.SYS_Flg.bit1)
#define	F_WORK_START			(U_Flage1.SYS_Flg.bit2)
#define	F_CHARGE_H_IO			(U_Flage1.SYS_Flg.bit3)
#define	F_CHARGE				(U_Flage1.SYS_Flg.bit4)
#define	F_CHARGE_FULL			(U_Flage1.SYS_Flg.bit5)
#define	F_FIRST_POWER_UP		(U_Flage1.SYS_Flg.bit6)
/**************** ¶¨Òå¼Ä´æÆ÷ ******************/

extern uint8_t r_g_workMod;


#endif