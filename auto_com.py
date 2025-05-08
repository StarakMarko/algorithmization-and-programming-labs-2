import keyboard
from lab7 import build_trie

trie = build_trie("dict.txt")

current_text = ""
word_buffer = ""
suggestions = []
chosen_index = -1


def clear_lines(n=2):
    for _ in range(n):
        print("\033[2K\r", end="", flush=True)
        print("\033[1A", end="", flush=True)


def show_input_and_suggestions():
    print(f"text: {current_text}{word_buffer}")
    if suggestions:
        sug_line = "suggestions: " + "  ".join(
            [f"{i+1}) {w}" for i, w in enumerate(suggestions)]
        )
    else:
        sug_line = "suggestions: (none)"
    print(sug_line)


def main():
    global current_text, word_buffer, suggestions, chosen_index

    print("To exit, type '_exit_' or press Ctrl+C")

    try:
        while True:
            clear_lines(2)
            full_text = (current_text + word_buffer).strip()
            last_word = full_text.split()[-1] if full_text else ""
            suggestions = trie.starts_with(last_word)[:5] if last_word else []
            show_input_and_suggestions()

            event = keyboard.read_event()
            if event.event_type != keyboard.KEY_DOWN:
                continue

            name = event.name
            if name == "enter":
                if (current_text + word_buffer).strip().lower() == "_exit_":
                    print("\nEXIT")
                    break
                current_text += word_buffer + " "
                word_buffer = ""
                print(f"\nnew text: {current_text.strip()}")
            elif name == "backspace":
                if word_buffer:
                    word_buffer = word_buffer[:-1]
                elif current_text:
                    current_text = " ".join(current_text.strip().split()[:-1]) + " "
            elif name == "space":
                current_text += word_buffer + " "
                word_buffer = ""
            elif len(name) == 1:
                word_buffer += name
            elif name == "esc":
                print("\nEXIT")
                break

            for i in range(1, 6):
                if keyboard.is_pressed(f"ctrl+{i}"):
                    chosen_index = i - 1
                    break

            if chosen_index != -1 and chosen_index < len(suggestions):
                current_text = (
                    " ".join((current_text + word_buffer).strip().split()[:-1])
                    + " "
                    + suggestions[chosen_index]
                    + " "
                )
                word_buffer = ""
                print(f"\nnew text: {current_text.strip()}")
                chosen_index = -1

    except KeyboardInterrupt:
        print("\nEXIT")


main()
