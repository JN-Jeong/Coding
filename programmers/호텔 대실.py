"""
호텔 대실
"""


def solution(book_time):
    answer = 1

    def time2min(time):
        result = []
        for t in time:
            hour, minute = t.split(":")
            result.append(int(hour) * 60 + int(minute))
        result[1] += 10
        return result

    books = []
    for t in book_time:
        books.append(time2min(t))
    sorted_books = sorted(books, key=lambda x: x[1])
    # print("@", sorted_books)

    for i in range(len(sorted_books)):
        start, end = sorted_books[i]
        result = 1
        for j in range(len(sorted_books)):
            if i == j:
                continue
            left, right = sorted_books[j]
            if left < end <= right:
                result += 1

        answer = max(answer, result)

    return answer


if __name__ == "__main__":
    book_time = [
        [
            ["15:00", "17:00"],
            ["16:40", "18:20"],
            ["14:20", "15:20"],
            ["14:10", "19:20"],
            ["18:20", "21:20"],
        ],
        [["09:10", "10:10"], ["10:20", "12:20"]],
        [["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]],
    ]
    answer = [3, 1, 3]

    for i, data in enumerate(book_time):
        b = data
        print(f"#{i}", solution(b))
