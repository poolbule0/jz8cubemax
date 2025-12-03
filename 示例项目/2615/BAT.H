#ifndef _BTA_H_
#define _BAT_H_

#include "ADC.h" 
#include "type.h" 
#include "main.h"


#define  D_CHECK_BAT_VAL_NUM           100 

#define D_BAT_VAL_CNT_SHK   30  
#define D_BAT_VAL_ADD_SHK   25 
#define D_BAT_VAL_DEC_SHK   25  

extern uint8_t r_g_batVal;				
extern uint8_t r_buff;


void sw_adcBatVal(void);


#endif