def solution(message, spoiler_ranges):
    answer = 0
    original_message = message.split(" ")
    message = list(message)
    for spoiler_range in spoiler_ranges:
        for i in range(spoiler_range[0], spoiler_range[1] + 1):
            if message[i] != " ":
                message[i] = "*"
    inspector = set()
    message = "".join(message).split(" ")
    for word in message:
        if "*" not in word:
            inspector.add(word)
    for i in range(len(message)):
        if "*" in message[i]:
            message[i] = original_message[i]
            if message[i] not in inspector:
                answer += 1
                inspector.add(message[i])
    return answer