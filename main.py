# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def get_input(word_type: str):
    user_input: str = input(f'Enter a {word_type}:')
    return user_input


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    first_noun = get_input('noun')
    first_verb = get_input('verb')
    adjective = get_input('adjective')
    sec_noun = get_input('noun')
    sec_verb = get_input('verb')

    story = f'''Once upon a time, there was a {adjective} {first_noun} who loved to {first_verb} all day.
    One day, {sec_noun} walked into the room and caught the {first_noun} in the act.

    {sec_noun}: "What are you doing?"
    {first_noun}: "I'm just {first_verb}ing, what's the big deal?"
    {sec_noun}: "Well, it's not every day that you see a {first_noun} {first_verb}ing in the middle of the day." 
    {first_noun}: "I guess you're right. Maybe I should take a break." 
    {sec_noun}: "That's probably a good idea. Why don't we go {sec_verb} instead?"
    {first_noun}: "Sure, that sounds like fun!"

    And so, {sec_noun} and the {first_noun} went off to {sec_verb} and had a great time.
    The end.
    '''

    print(story)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
