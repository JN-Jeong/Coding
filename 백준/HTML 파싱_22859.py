import re


def solution():
    html = input().replace("<main>", "").replace("</main>", "")

    div_pattern = re.compile(r'<div title="(.+?)">(.+?)</div>', re.DOTALL)
    p_pattern = re.compile(r"<p>(.+?)</p>", re.DOTALL)

    div_matches = div_pattern.findall(html)
    # print(div_matches)
    for div_match in div_matches:
        title = div_match[0]
        print(f"title : {title}")

        p_matches = p_pattern.findall(div_match[1])
        # print(p_matches)
        for p_match in p_matches:
            print(re.sub(r" {2,}", " ", re.sub(r"<.*?>", "", p_match).strip()))


if __name__ == "__main__":
    solution()
