#include "sleep.h"
unsigned char sleep_cnt = 0;
void sleep_event()
{
    if(F_CHARGE == 0)
    {
        if(sleep_cnt++ > 10)
        {
            sleep_cnt = 0;
            //TCC=0;
            //CONTW(0X0F);		//预分频，分配给WDT (PAB == 1)
            LVDCON = 0;// 关LVD

            IOCP_W(IMR,0x00);   //关闭中断
            IOCP_W(WDTCR,0x00);	
            ISR	=0;              // 清中断标志位
            DI();		         // 禁止唤醒进入中断
            IOCP_W(IMR,0x02);    //使能端口变化中断，不使能无法唤醒
            SLEEP();
            NOP(); 
            NOP();
            NOP();
            NOP();
            CWDT();
        //------------睡眠唤醒----------------------
            // CONTW(0x02);        //TCC 8分频
            // IOCP_W(WDTCR,0x00); //关闭看门狗
            // IOCP_W(IMR,0x01);   //开启定时器中断
            // TCC = data_tcc;
            IOCP_W(IMR,0x00);   //关闭中断
            fw_tc0Init();
            EI();
            ISR=0;
        }

    }


}