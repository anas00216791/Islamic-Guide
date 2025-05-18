from chainlit import user_session

class Question:
    def __init__(self, question: str, answer: str):
        self.question = question.lower().strip()
        self.answer = answer

    def matches(self, user_question: str) -> bool:
        return self.question == user_question.lower().strip()


class IslamicQABot:
    def __init__(self, name="Anas Tariq"):
        self.name = name
        self.questions = []
        self.load_default_questions()

    def load_default_questions(self):
            self.add_question("What is Zakat", "Zakat is 2.5% of savings given to the needy. It is one of the five pillars of Islam.")
            self.add_question("How many daily prayers are there", "There are five daily prayers: Fajr:(04:00 AM – 05:30 AM), Dhuhr:(12:00 PM – 01:30 PM), Asr:(04:30 PM – 05:00 PM), Maghrib:(06:30 PM – 07:15 PM), and Isha:(08:00 PM – 09:30 PM)")
            self.add_question("Who is the last prophet", "The last Prophet is Muhammad (peace be upon him).")
            self.add_question("What is Ramadan", "Ramadan is the 9th month of the Islamic calendar. Muslims fast from dawn till sunset during this month.")
            self.add_question("What is Hajj", "Hajj is the pilgrimage to Makkah and is obligatory once in a lifetime for those who are able.")
            self.add_question("What is the Quran", "The Quran is the holy book of Islam revealed to Prophet Muhammad (PBUH).")
            self.add_question("What is the Kaaba", "The Kaaba is a sacred building in Makkah toward which Muslims face during prayer.")
            self.add_question("What is Tawheed", "Tawheed is the oneness of Allah. It is the belief that Allah is One without partners.")
            self.add_question("What is Shirk", "Shirk is associating partners with Allah, which is a major sin in Islam.")
            self.add_question("Who are the Sahaba", "The Sahaba were the companions of Prophet Muhammad (PBUH).")
            self.add_question("What is Hadith", "Hadith is the collection of sayings and actions of Prophet Muhammad (PBUH).")
            self.add_question("What is Sunnah", "Sunnah is the way and teachings of Prophet Muhammad (PBUH).")
            self.add_question("What is Halal", "Halal refers to what is permissible or lawful in Islam.")
            self.add_question("What is Haram", "Haram refers to what is forbidden or prohibited in Islam.")
            self.add_question("How many Surahs are there in the Quran", "There are 114 Surahs in the Quran.")
            self.add_question("What is the first Surah in the Quran", "The first Surah is Al-Fatiha.")
            self.add_question("What is Laylatul Qadr", "Laylatul Qadr is the Night of Decree, better than a thousand months, in the last ten nights of Ramadan.")
            self.add_question("What breaks wudu", "Things like using the toilet, deep sleep, or passing wind break wudu.")
            self.add_question("How to perform wudu", "Wudu includes washing the hands, mouth, nose, face, arms, wiping the head, and washing the feet.")
            self.add_question("What is the meaning of Islam", "Islam means submission to the will of Allah.")
            self.add_question("Who is Allah", "Allah is the one and only God, the Creator and Sustainer of the universe.")
            self.add_question("What is Iman", "Iman means faith. It is belief in Allah, His angels, His books, His messengers, the Last Day, and Qadr.")
            self.add_question("What is the Qibla", "The Qibla is the direction Muslims face during prayer, which is toward the Kaaba in Makkah.")
            self.add_question("What is Jannah", "Jannah is Paradise, the eternal home of bliss for the righteous in the Hereafter.")
            self.add_question("What is Jahannam", "Jahannam is Hell, the place of punishment for disbelievers and sinners.")
            self.add_question("What is the Day of Judgment", "The Day of Judgment is when all people will be resurrected and judged by Allah for their deeds.")
            self.add_question("Who is the Angel Jibreel", "Angel Jibreel (Gabriel) brought revelation from Allah to the prophets.")
            self.add_question("How do Muslims greet each other", "Muslims greet each other with 'As-salamu Alaikum' meaning 'Peace be upon you'.")
            self.add_question("What is Dua", "Dua is supplication or calling upon Allah.")
            self.add_question("What is Sadaqah", "Sadaqah is voluntary charity given for the sake of Allah.")
            self.add_question("What is the significance of Friday", "Friday is a blessed day for Muslims, and the weekly congregational prayer (Jumu'ah) is held on this day.")
            self.add_question("What is the meaning of Alhamdulillah", "Alhamdulillah means 'All praise is due to Allah'.")
            self.add_question("What is the meaning of Bismillah", "Bismillah means 'In the name of Allah'. It is recited before starting any task.")
            self.add_question("What is the meaning of InshaAllah", "InshaAllah means 'If Allah wills'. It is used when talking about future events.")
            self.add_question("What is the meaning of MashaAllah", "MashaAllah means 'As Allah has willed'. It is used to express appreciation or admiration.")
            self.add_question("What is the meaning of SubhanAllah", "SubhanAllah means 'Glory to Allah. It is used to express amazement or admiration for Allah's creation.") 


    def add_question(self, question: str, answer: str):
        self.questions.append(Question(question, answer))

    def get_answer(self, user_question: str) -> str:

        # Default: search questions
        for q in self.questions:
            if user_question.lower() in q.question.lower():
                return q.answer
        return "Sorry, I don't know the answer to that."

    def start_chat(self):
        print(f" Assalamu Alaikum! I am {self.name}, your Islamic Q&A Bot.")
        print("Ask me something about Islam or type 'exit' to quit.\n")

        while True:
            user_input = input("You: ")
            if user_input.lower().strip() in ["exit", "quit", "bye"]:
                print("Bot: Wa Alaikum Assalam. May Allah bless you.")
                break

            answer = self.get_answer(user_input)
            print(f"Bot: {answer}")
def load_default_questions(self):

    def add_question(self, question: str, answer: str):
        self.questions.append(Question(question, answer))

def get_answer(self, user_question: str) -> str:
    user_question = user_question.lower().strip()

    for q in self.questions:
        if q.matches(user_question):
            return q.answer

    return "I'm sorry, I don't have an answer to that. Please consult a knowledgeable scholar."
if __name__ == "__main__":
    bot = IslamicQABot()
    bot.start_chat()
