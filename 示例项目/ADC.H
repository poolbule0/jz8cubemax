#ifndef _FW_ADC_H_
#define _FW_ADC_H_

#include "type.h"

// ADC数据定义
enum
{
      E_AD0_P50 = 0,
      E_AD1_P51,
      E_AD2_P52,
      E_AD3_P53,
      E_AD4_P54,
      E_AD5_P55,
      E_AD6_P60,
      E_AD7_P61,
      E_AD8_P62,
      E_AD9_P63,
      E_AD10_P64,
      E_AD11_P65,
      E_AD12_P66,
      E_AD13_P67,
      E_AD14,
};
enum
{
    E_Vrefh_VDD = 0,						//; ADC reference high voltage is VDD
	E_Vrefh_4V,							//; ADC reference high voltage is 4V	
	E_Vrefh_3V,							//; ADC reference high voltage is 3V	
	E_Vrefh_2V,					          //; ADC reference high voltage is 2V
    E_Vrefh_1_5V,					          //; ADC reference high voltage is 1.5V
};
#define		C_Ckl_Div16					0x00			//; ADC clock is Fosc/16
#define		C_Ckl_Div4					0x40			//; ADC clock is Fosc/4	
#define		C_Ckl_Div64					0x80			//; ADC clock is Fosc/64
#define		C_Ckl_Div1					0xC0           //; ADC clock is Fosc/1

#define		C_ADC_START					0x40           //; ADC Start

#define    DELAY_TIME    3000

uint16_t 	ADC_GetValue(uint8_t chn,uint8_t vref);

#endif