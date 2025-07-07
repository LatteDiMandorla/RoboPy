TARGET = server

SRCS = server.c personality_picker.c

OBJS = $(SRCS:.c=.o)

LIBS = -lcurl -lcjson

CC = gcc

CFLAGS = -Wall -g

all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(OBJS) -o $@ $(LIBS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(TARGET)
