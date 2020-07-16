#include "main.h"

#include <cstdint>

AsyncMqttClient mqtt;
AsyncClient client;

void setup() {

    Serial.begin(115200);

    WiFi.begin("SSID", "PASS");

    mqtt.connect();
    mqtt.publish("test", 0, false, "test");

    client.onConnect([](void*, AsyncClient* c) {
        c->write("teststring");
        c->close(); 
    });
    client.onError([](void*, AsyncClient* c, int8_t err) {
        Serial.printf(PSTR("Error %s (%d) on client %p\n"), c->errorToString(err), err, c);
    });
    client.connect("foo.bar", 80);

}

void loop() {
}
