#ifndef _USER_H_
#define _USER_H_

#include "type.h"
#include "pwm.h"
#include "sleep.h"



/*********** 数据定义 ***************/
#define   T_1MS             6
#define   TCC_TIM           T_1MS

#define   D_10MS            1


/*********** 端口定义 ***************/
#define   IO_KEY        PORT6_4

/*********** 标志位定义 *************/
typedef struct SYS_FlgBit_
{   
    uint8_t BIT0:1;              // 10ms
    uint8_t BIT1:1;
    uint8_t BIT2:1;
    uint8_t BIT3:1;
    uint8_t BIT4:1;
    uint8_t BIT5:1;
    uint8_t BIT6:1;
    uint8_t BIT7:1;
}SYS_FlgBit;
typedef union SYS_FlgBitClass_
{
    uint8_t       FlgAll;
    SYS_FlgBit    SYS_Flg;
}SYS_FlgBitClass;

extern SYS_FlgBitClass U_Flage;
#define    Time_10ms          (U_Flage.SYS_Flg.BIT0) 
#define    F_CHARGE        (U_Flage.SYS_Flg.BIT1) 
#define    F_CHARGE_FULL   (U_Flage.SYS_Flg.BIT2) 
#define    F_CHARGE_H_IO   (U_Flage.SYS_Flg.BIT3) 
#define    dir			   (U_Flage.SYS_Flg.BIT4) 

/*********** 寄存器*************/
extern uint8_t r_g_workMod;

/*********** 函数 *************/
void fw_clrRam(void);
void fw_gpioInit(void);
void fw_tc0Init(void);

#endif

