#ifndef _PWM_H_
#define _PWM_H_

#include "user.h"
enum
{
    E_PWM_DIV_1 = 0x00,
    E_PWM_DIV_2 = 0X08,
    E_PWM_DIV_4,
    E_PWM_DIV_8,
    E_PWM_DIV_16,
    E_PWM_DIV_32,
    E_PWM_DIV_64,
    E_PWM_DIV_128,
    E_PWM_DIV_256,
};
#define    D_PWM_DIV_SLCT     E_PWM_DIV_1    // PWM·ÖÆµÑ¡Ôñ

void pwm1Init();
void pwm2Init();
void pwm3Init();
#endif