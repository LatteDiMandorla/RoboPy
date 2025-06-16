#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>
#include "../src/utilities.c"


struct memory {
  char * response;
  size_t size    ;
};

size_t write_callback(char * ptr, size_t size, size_t nmemb, void * userdata) {
  size_t realsize = size * nmemb;
  struct memory * mem = (struct memory *)userdata;

  char * data = realloc(mem->response, mem->size + realsize + 1);
  if(!data) return 0;

  mem->response = data;
  memcpy(&(mem->response[mem->size]), ptr, realsize);
  mem->size += realsize;
  mem->response[mem->size] = 0;

  return realsize;
}


char * ask_chatGPT(const char * prompt) {
  CURL * curl = curl_easy_init();

  char * API_KEY = read_api(".env");

  if (!curl) return NULL;

  struct memory chunk;

  chunk.response = malloc(1);
  chunk.size     = 0;

  const char * url = "https://api.openai.com/v1/chat/completations";

  char postdata[2048];
  snprintf(postdata, sizeof(postdata),
           "{\"model\": \"gpt-3.5-turbo\", \"messages\": [{\"role\": \"user\", \"content\": \"%s\"}]}",
           prompt);

  struct curl_slist * headers = NULL;
  headers = curl_slist_append(headers, "Content-Type: application/json");

  char auth[256];
  snprintf(auth, sizeof(auth), "Authorization: Bearer %s", API_KEY);
  headers = curl_slist_append(headers, auth);

  curl_easy_setopt(curl, CURLOPT_URL, url);
  curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
  curl_easy_setopt(curl, CURLOPT_POSTFIELDS, postdata);
  curl_easy_setopt(curl, CURLOPT_WRITEDATA, (void *)&chunk);
  curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);

  CURLcode res = curl_easy_perform(curl);
  if (res != CURLE_OK) {
    fprintf(stderr, "Error curl: %s\n", curl_easy_strerror(res));
    curl_easy_cleanup(curl);
    return NULL;
  }

  curl_easy_cleanup(curl);
  curl_slist_free_all(headers);

  return chunk.response;
  

}

void url_encode(const char * src, char * dst, size_t dst_size) {
    size_t j = 0;

    /* The cicle continues until the end of the string and there's still some 
     * space to write. If the char is a space, then %20 is inserted. */ 

    for (size_t i = 0; src[i] != '\0' && j + 3 < dst_size; i++) {
        if (src[i] == ' ') {
            dst[j++] = '%';
            dst[j++] = '2';
            dst[j++] = '0';
        } else {
            dst[j++] = src[i];
        }
    }
    dst[j] = '\0';
}

void furhat_say(const char *furhat_ip, const char *text) {
    CURL *curl;
    CURLcode res;

    char encoded_text[512];
    url_encode(text, encoded_text, sizeof(encoded_text));

    char url[1024];
    snprintf(url, sizeof(url), "http://%s:54321/furhat/say?text=%s", furhat_ip, encoded_text);
    
    curl = curl_easy_init();
    if(curl) {
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_POST, 1L);
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, "");  
        curl_easy_setopt(curl, CURLOPT_POSTFIELDSIZE, 0); 
        curl_easy_setopt(curl, CURLOPT_CONNECTTIMEOUT, 5L);
        curl_easy_setopt(curl, CURLOPT_TIMEOUT, 5L);
        
        res = curl_easy_perform(curl);

        if(res != CURLE_OK) {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        }

        curl_easy_cleanup(curl);
    }
}

int main() {
    const char *furhat_ip = "192.168.1.20"; 
    const char *message_from_chatgpt = "Hello there!";

    furhat_say(furhat_ip, message_from_chatgpt);

    printf("\n");
    return 0;
}
