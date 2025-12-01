#ifndef __PWM_H__
#define __PWM_H__

#include "type.h"
#include "main.h"

//PWM∂®“Â 
#define     TC0_ENABLE           ENABLE
#define     PWM1_ENABLE          DISABLE
#define     PWM2_ENABLE          ENABLE
#define     PWM3_ENABLE          DISABLE
#define     PWM4_ENABLE          DISABLE
enum  //PWM clock config
{
    E_PWM_DIV_1 = 0,
    E_PWM_DIV_2,
    E_PWM_DIV_4,
    E_PWM_DIV_8,
    E_PWM_DIV_16,
    E_PWM_DIV_64,
    E_PWM_DIV_128,
    E_PWM_DIV_256,
};

enum  //TC0 clock config
{
    E_TC0_DIV_2,
    E_TC0_DIV_4,
    E_TC0_DIV_8,
    E_TC0_DIV_16,
    E_TC0_DIV_32,
    E_TC0_DIV_64,
    E_TC0_DIV_128,
    E_TC0_DIV_256,
};

// /*************** pwm1/3 freq config ********************/
#define    SET_PWM13_FREQ(x)      {TC1PRDTH = 0;TC1PRDL =  x;}

/*************** pwm1 duty config ********************/
#define    SET_PWM1_DUTY(x)      {TC1PRDTH = 0;	PWM1DTL =  x;}

/*************** PWM1 enable control *****************/
#define    SET_PWM1_DISABLE()      {PWM1E = DISABLE;PORT6_0 = 0;}

#define    SET_PWM1_ENABLE()        {PWM1E = ENABLE;}

/*************** pwm3 duty config ********************/
#define    SET_PWM3_DUTY(x)      {PWM3DTH = 0;PWM3DTL =  x;}

/*************** PWM3 enable control *****************/
#define    SET_PWM3_DISABLE()      {PWM3E = DISABLE;PORT5_1 = 0;}

#define    SET_PWM3_ENABLE()       {PWM3E = ENABLE;}



// /*************** pwm2/4 freq config ********************/
#define    SET_PWM24_FREQ(x)      {TC2PRDTH = 0;TC2PRDL =  x;}

/*************** pwm2 duty config ********************/
#define    SET_PWM2_DUTY(x)      {TC2PRDTH = 0;	PWM2DTL =  x;}

/*************** PWM2 enable control *****************/
#define    SET_PWM2_DISABLE()      {PWM2E = DISABLE;PORT6_1 = 0;}

#define    SET_PWM2_ENABLE()        {PWM2E = ENABLE;}

/*************** pwm4 duty config ********************/
#define    SET_PWM4_DUTY(x)      {PWM4DTH = 0;PWM4DTL =  x;}

/*************** PWM4 enable control *****************/
#define    SET_PWM4_DISABLE()      {IPWM4E = DISABLE;PORT5_1 = 0;}

#define    SET_PWM4_ENABLE()        {IPWM4E = ENABLE;}

void fw_tc0Init(void);
void fw_pwm2Init(void);
void fw_pwm4Init(void);
void fw_pwm1Init(void);
void fw_pwm3Init(void);
#endif