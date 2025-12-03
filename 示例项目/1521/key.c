#include "key.h"
#include "user.h"

// 全局变量
uint8_t keyLongCnt = 0;
uint8_t keyValOld = 0;
uint8_t keyState = 0;
uint8_t keyShake = 0;

// 简化版按键扫描函数
uint8_t keyScan(void)
{
    uint8_t keyVal = 0;
    uint8_t keyEvent = 0;
    
    // 检测按键是否按下（PORT6_0低电平表示按下）
    if(PORT6_0 == 0)
    {
        keyVal = 1;  // 按键按下
    }

    switch(keyState)
    {
        // 状态0：等待按键按下
        case 0:
            keyShake = 0;
            keyValOld = 0;
            keyLongCnt = 0;
            
            if(keyVal)
            {   
                keyValOld = keyVal;
                keyState = 1;  // 进入消抖状态
            }
            break;
            
        // 状态1：按键消抖
        case 1:
            if(keyVal == keyValOld)
            {
                if(++keyShake >= 3)  // 消抖3次
                {
                    keyShake = 0;
                    keyState = 2;  // 进入长按检测
                }
            }
            else  
            {
                keyState = 0;  // 按键抖动，返回初始状态
            }
            break;
            
        // 状态2：长按检测
        case 2:
            if(keyVal == keyValOld)
            {
                keyShake = 0;
                if(++keyLongCnt >= 200)  // 长按时间约2秒
                {
                    keyLongCnt = 0;
                    keyEvent = 0x40;  // 长按事件
                    keyState = 3;     // 进入等待抬起状态
                }
            }
            else if(keyVal == 0)
            {
                if(++keyShake >= 3)
                {
                    keyShake = 0;
                    keyEvent = 0x80;  // 短按事件
                    keyState = 0;     // 返回初始状态
                }
            }
            else
            {
                keyShake = 0;
                keyState = 0;  // 异常情况
            }
            break;
            
        // 状态3：等待按键抬起
        case 3:
            keyValOld = 0;
            if(keyVal == 0)
            {
                if(++keyShake >= 3)
                {
                    keyShake = 0;
                    keyState = 0;  // 按键抬起，返回初始状态
                }
            }
            else
            {
                keyShake = 0;
            }
            break;
            
        default:
            keyState = 0;
            break;
    }

    return keyEvent;
}

// 简化版软件按键处理
void keyProcess(void)
{
    uint8_t keyEvent = keyScan();

    // 短按事件处理
    if(keyEvent & 0x80)  // 短按
    {
        F_CHARGE ^= 1;   // 切换充电状态
        PORT6_5 ^= 1;    // 切换LED指示
    }
    
    // 长按事件处理
    if(keyEvent & 0x40)  // 长按
    {
        static uint8_t light = 0;
		if(PDC1 >= 0x64)
		{
			dir = 0;
		}
		else
		{
			dir = 1;
		}
        // 根据方向调整亮度
        if(dir == 1)
        {
            // 增加亮度
            if(light <= 100)  // 防止溢出
                light += 10;
            else
                light = 100;
        }
        else
        {
            // 减少亮度
            if(light > 0)   // 防止下溢
                light -= 10;
            else
                light = 0;
        }
        
        // 更新PWM值
        PDC1 = light;
		
        PORT6_4 ^= 1;    // 切换LED指示
    }
}