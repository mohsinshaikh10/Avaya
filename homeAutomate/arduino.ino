String inputCommand;
const int bed = 12;
const int liv = 13;
void setup()  
{  
    Serial.begin(9600);   
    Serial.print("connection Successfull"); 
	pinMode(bed, OUTPUT);
	pinMode(liv, OUTPUT);
}

void loop()
{
	while(Serial.available()>0)
	{ 
		inputCommand=Serial.read();
		if(inputCommand == "bedON")
		{
			digitalWrite(bed, HIGH);
		}
		else if(inputCommand == "bedOFF")
		{
			digitalWrite(bed, LOW);
		}
		else if(inputCommand == "livON")
		{
			digitalWrite(liv, HIGH);
		}
		else if(inputCommand == "livOFF")
		{
			digitalWrite(liv, LOW);
		}
	}
}