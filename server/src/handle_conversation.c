#include "handle_conversation.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>



const char* introvert_gesture = "{                                  \
  \"name\": \"IntrovertNod\",                                       \
  \"frames\": [                                                     \
    {                                                               \
      \"time\": [0.3, 1.0],                                         \
      \"params\": {                                                 \
        \"NECK_TILT\": 5.0,                                         \
        \"SMILE_CLOSED\": 0.2,                                      \
        \"BROW_IN_LEFT\": 0.5,                                      \
        \"BROW_IN_RIGHT\": 0.5,                                     \
        \"LOOK_DOWN\": 1.0                                          \
      }                                                             \
    },                                                              \
    {                                                               \
      \"time\": [2.0],                                              \
      \"params\": { \"reset\": true }                               \
    }                                                               \
  ],                                                                \
  \"class\": \"furhatos.gestures.Gesture\"                          \
}";



void send_gesture(const char* gesture_json) {
    CURL *curl;
    CURLcode res;

    curl = curl_easy_init();
    if (curl) {
        struct curl_slist *headers = NULL;

        headers = curl_slist_append(headers, "Content-Type: application/json");

        curl_easy_setopt(curl, CURLOPT_URL, "http://192.168.1.6:54321/furhat/gesture");
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, gesture_json);
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);

        res = curl_easy_perform(curl);

        if (res != CURLE_OK)
            fprintf(stderr, "Errore nella richiesta: %s\n", curl_easy_strerror(res));

        curl_easy_cleanup(curl);
    }
}



int main() {

    /* Considering to refactor this, and probably use docker network or give this responsability to client. */
    const char *furhat_ip = "192.168.1.20"; 

    send_gesture(introvert_gesture);

    printf("\n");
    return 0;
}
