/*
在此处进行工作模式的判断。有两种模式，一种为充电模式一种为放电模式
充电模式就是将标志位F_CHARGE置1
放电模式就是将寄存器r_g_workMod置1
充电模式下，然后此时判断P65的状态，如果P65为低电平则表示当前是充电状态，此时数码管应该显示充电的指示灯。
放电模式下，也就是判断按键是否按下了，如果P63按下按键，则表示为放电状态，此时数码管应该显示放电，充电指示灯不亮。
*/

#include "mode.h"
#include "main.h"


unsigned char s_charge_cnt ;  // 充电输入低电平稳定计数
unsigned char s_charge_full_cnt ;  // 充电满低电平稳定计数
unsigned char s_key_cnt    ;  // 放电按键低电平稳定计数
unsigned char key_state    ;  // 按键状态（0=未按下，1=已按下且去抖完成）
unsigned char key_last     ;  // 上一次按键状态（用于边沿检测）


// 工作模式判断函数
void Mode_Check(void)
{
    // 优先对充电IO进行去抖
    if (Io_Charge == 0 )
    {
        if (++s_charge_cnt >= 15)
        {
            // 确认进入充电模式
            F_CHARGE = 1;
            r_g_workMod = 0;
            // 避免按键去抖计数残留导致误触发
            s_key_cnt = 0; 
        }
    }
    else
    {
        s_charge_cnt = 0;
        F_CHARGE = 0;
    }

    if(Io_Charge_full == 0)
    {
        if (++s_charge_full_cnt >= 15)
        {
            F_CHARGE_FULL = 1;
            r_g_workMod = 0;
            F_CHARGE = 1;
            s_charge_cnt = 0;
            s_key_cnt = 0;
            
        }
    }
    else
    {
        s_charge_full_cnt = 0;
        F_CHARGE_FULL = 0;
    }

    // 充电未确认，则对按键进行去抖
    if (Io_Key == 0)
    {
        if (++s_key_cnt >= 15)
        {
            key_state = 1;
        }
    }
    else
    {
        s_key_cnt = 0;
        key_state = 0;
    }
    
    // 按键边沿检测：检测从0到1的跳变（按键从未按下到已按下）
    if (key_state == 1 && key_last == 0)
    {
        // 按键按下边沿触发，切换工作模式
        F_CHARGE = 0;
        r_g_workMod = (r_g_workMod == 0) ? 1 : 0;  // 状态切换
    }
    
    // 更新上一次按键状态
    key_last = key_state;

}
