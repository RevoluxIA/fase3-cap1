#include <DHT.h> // Biblioteca para sensor de temperatura e umidade DHT

// Definição dos pinos conectados aos sensores e atuadores
#define DHTPIN 27         // Pino de dados do sensor DHT22 (temperatura e umidade)
#define DHTTYPE DHT22     // Define o tipo do sensor como DHT22
#define LDRPIN 25         // Pino analógico do LDR (simulando sensor de pH)
#define RELAYPIN 26       // Pino de controle do relé (bomba d'água)
#define LEDPIN 19         // Pino do LED indicador de irrigação

DHT dht(DHTPIN, DHTTYPE); // Instancia o sensor DHT

void setup() {
  Serial.begin(115200); // Inicializa a comunicação serial para depuração
  dht.begin();          // Inicializa o sensor DHT22
  
  // Configura os botões com resistor pull-up interno ativado
  pinMode(14, INPUT_PULLUP); // Botão para simular presença de fósforo
  pinMode(12, INPUT_PULLUP); // Botão para simular presença de potássio
  
  // Configura os pinos do relé e do LED como saída
  pinMode(RELAYPIN, OUTPUT); 
  pinMode(LEDPIN, OUTPUT);   
}

void loop() {
  delay(2000); // Aguarda 2 segundos entre as leituras

  // Leitura dos botões (lógica invertida por uso de pull-up)
  int buttonPhosphorus = digitalRead(14);     // Leitura do botão de fósforo
  int buttonPotassium = digitalRead(12);      // Leitura do botão de potássio
  bool phosphorusPresent = !buttonPhosphorus; // Verdadeiro se botão pressionado
  bool potassiumPresent = !buttonPotassium;   // Verdadeiro se botão pressionado

  // Leitura dos sensores de umidade e temperatura
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  // Leitura do valor do sensor LDR (simulando sensor de pH)
  int ldrValue = analogRead(LDRPIN);
  
  // Verifica se houve falha na leitura do sensor DHT22
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Falha ao ler do sensor DHT22!");
    return; // Sai da função se leitura falhou
  }

  // (Este teste é desnecessário, pois analogRead nunca retorna NaN, mas deixado aqui para consistência)
  if (isnan(ldrValue)){
    Serial.println("Falha ao ler do sensor LDR");
  }

  // Converte o valor do LDR para uma escala de 0 a 14 (simulando pH)
  float pH = (ldrValue / 4095.0) * 14.0; 

  // Exibe os dados lidos no monitor serial
  Serial.print("Umidade: ");
  Serial.print(humidity);
  Serial.print("%  Temperatura: ");
  Serial.print(temperature);
  Serial.println("°C");

  Serial.print("pH: ");
  Serial.println(pH);

  Serial.print("Valor do sensor (LDR): ");
  Serial.println(ldrValue);

  // ---------- Lógica de Irrigação Inteligente ----------

  // Se a umidade estiver baixa e o pH estiver adequado
  if (humidity < 30 && pH >= 6 && pH <= 8) {
    digitalWrite(RELAYPIN, HIGH); // Liga a bomba de irrigação
    digitalWrite(LEDPIN, HIGH);   // Acende o LED indicando irrigação ativa
    Serial.println("Bomba LIGADA");

    // Verifica se o botão de potássio está pressionado
    if(potassiumPresent){
      Serial.println("Adicionando Potássio"); // Indica adição de potássio
    }

    // Verifica se o botão de fósforo está pressionado
    if(phosphorusPresent){
      Serial.println("Adicionando Fósforo"); // Indica adição de fósforo
    }

  } else {
    // Se as condições não forem atendidas, desliga a bomba e o LED
    digitalWrite(RELAYPIN, LOW);  
    digitalWrite(LEDPIN, LOW);    
    Serial.println("Bomba DESLIGADA");
  }
}
