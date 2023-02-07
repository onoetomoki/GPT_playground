######################################################
#
#  Local Conversation between ChatGPT by openAI
#      2023.01.15 T.Onoe
#
#  To use: python (this filename).py
#          Enter a promot: (The contents of question)
#
######################################################


import openai
import os
import datetime
import time


def main():
    openai.api_key = "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"
    now = datetime.datetime.now()
    os.mkdir(f"../output/{now.strftime('%Y%m%d_%H%M%S')}")
#    outtext = []

    # First question
    print("Beginning of conversation")
    prompt = input("何について質問しますか?：")
    if prompt == "n":
        return

    f = open(f"../output/{now.strftime('%Y%m%d_%H%M%S')}/question.txt", "w")
    f.write(str(prompt))
    f.close()

    prompt = "以下のことについて詳しく教えて下さい。:" + prompt
    out = GPTengine(prompt)
    f = open(f"../output/{now.strftime('%Y%m%d_%H%M%S')}/output_file_0.txt", "w")
    out.replace("\n\n", "")
    f.write(str(out))
    f.close()
#    outtext.append(out)

    iterate = 10

    # Conversation
    for i in range(iterate):
        time.sleep(20)
        prompt2 = "以下のことについて詳しく教えて下さい。" + out
        #prompt2 = "Describe more detail" + out
        out = GPTengine(prompt2)
        out.replace("\n\n", "")
#        outtext.append(out)
        f = open(f"../output/{now.strftime('%Y%m%d_%H%M%S')}/output_file_{i+1}.txt", "w")
        f.write(str(out))
        f.close()


def GPTengine(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    for choice in completions.choices:
        print(choice.text)
        output = choice.text

    return output


if __name__ == "__main__":
    main()