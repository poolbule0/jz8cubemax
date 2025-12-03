#include "smg.h"
#include "bat.h"
//
/*p52,   p51,    p50,    p67,    p66
  smg_1, smg_2, smg_3,  smg_4,  smg_5
*/
Sys_FlagLed_Class	Flag_Led1;
Sys_FlagLed_Class	Flag_Led2;
Sys_FlagLed_Class	Flag_Led3;
Sys_FlagLed_Class	Flag_Led4;

uint8_t smg_cnt = 0;
//数码管段选码表  “0~9”  “空”
const uint8_t t_ledCntTab[] = 
{
    0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F,0x00
};

void SMG_Display(uint8_t a ,uint8_t b)
{
  uint8_t smg_bai = 10;
  uint8_t smg_shi = 0;
  uint8_t smg_ge = 0;
  uint8_t smg_tu = 0;
  uint8_t smg_buff = 0;

  smg_buff = a;
  smg_tu = b;
  if(smg_buff >= 100)
  {
    smg_bai = 1;
    smg_shi = 0;
    smg_ge = 0;
  }
  else 
  {
    while(smg_buff >= 10)
    {
      smg_buff -= 10;
      smg_shi++;
    }
    smg_ge = smg_buff;
  }

  smg_bai = t_ledCntTab[smg_bai];
  smg_shi = t_ledCntTab[smg_shi];
  smg_ge = t_ledCntTab[smg_ge];

  SMG_BAI = smg_bai;
  SMG_SHI = smg_shi;
  SMG_GE = smg_ge;
  SMG_TU = smg_tu;


}

void SMG_Scan(void)
{
 
  IO_IN();
  switch(smg_cnt)
  {
		case 0:
				if(B1_LED)
				{
					PIN3_H();
				}
				PIN4_L();
			break;
   		case 1:
				if (C1_LED)
				{
					PIN4_L();
				}
				PIN2_H();
			break;
		case 2:
				if (A2_LED)
				{
					PIN3_L();
				}
				PIN2_H();
			break;
		case 3:
				if (B2_LED)
				{
					PIN2_L();
				}
				PIN3_H();
			break;
		case 4:
				if (C2_LED)
				{
					PIN3_L();
				}
				PIN4_H();
			break;
		case 5:
				if (D2_LED)
				{
					PIN2_L();
				}
				PIN4_H();
			break;
		case 6:
				if (E2_LED)
				{
					PIN2_L();
				}
				PIN5_H();
			break;
		case 7:
				if (F2_LED)
				{
					PIN3_L();
				}
				PIN5_H();
			break;
		case 8:
				if (G2_LED)
				{
					PIN4_L();
				}
				PIN5_H();
			break;
		case 9:
				if (A3_LED)
				{
					PIN2_L();
				}
				PIN1_H();
			break;
		case 10:
				if (B3_LED)
				{
					PIN1_L();
				}
				PIN2_H();
			break;
		case 11:
				if (C3_LED)
				{
					PIN3_L();
				}
				PIN1_H();
			break;
		case 12:
				if (D3_LED)
				{
					PIN1_L();
				}
				PIN3_H();
			break;
		case 13:
				if (E3_LED)
				{
					PIN4_L();
				}
				PIN1_H();
			break;
		case 14:
				if (F3_LED)
				{
					PIN1_L();
				}
				PIN4_H();
			break;
		case 15:
				if (G3_LED)
				{
					PIN1_L();
				}
				PIN5_H();
			break;
		case 16:
				if (B_LED_LIGHTING)
				{
					PIN5_L();
				}
				PIN3_H();
			break;
		case 17:
				if (B_LED_PERCENT_SIGNS)
				{
					PIN5_L();
				}
				PIN2_H();
			break;


		default:
			break;
	}

	if (++ smg_cnt > 17)
	{
		smg_cnt = 0;
	}

}