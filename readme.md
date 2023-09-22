### potplayer 播放列表生成器

自动搜索指定目录下的所有视频文件并生成dpl播放列表文件

#### 用法
默认在当前目录搜索，默认文件格式为mp4

可以指定目录与文件格式

会在指定目录同级生成.dpl文件，用potplayer打开即可
```shell
C:\Users\Wangs\Desktop>python playlist.py -h
python playlist.py "filepath" "filetype"
default filepath is current directory
defaule filetype is ".mp4"
```
例如
```shell
C:\Users\Wangs\Desktop>python playlist.py "E:\学习\Udemy-100.Days.of.Code.The.Complete.Python.Pro.Bootcamp.for.2022"
path: E:\学习\Udemy-100.Days.of.Code.The.Complete.Python.Pro.Bootcamp.for.2022
filetype: .mp4
001 What you're going to get from this course.mp4
002 START HERE.mp4
003 Downloadable Resources and Tips for Taking the Course.mp4
004 Day 1 Goals_ what we will make by the end of the day.mp4
006 Printing to the Console in Python.mp4
007 [Interactive Coding Exercise] Printing.mp4
008 String Manipulation and Code Intelligence.mp4
009 [Interactive Coding Exercise] Debugging Practice.mp4
010 The Python Input Function.mp4
011 [Interactive Coding Exercise] Input Function.mp4
012 Python Variables.mp4
013 [Interactive Coding Exercise] Variables.mp4
014 Variable Naming.mp4
015 Day 1 Project_ Band Name Generator.mp4
016 Congratulations! Well done!.mp4
017 Day 2 Goals_ what we will make by the end of the day.mp4
018 Python Primitive Data Types.mp4
019 Type Error, Type Checking and Type Conversion.mp4
020 [Interactive Coding Exercise] Data Types.mp4
021 Mathematical Operations in Python.mp4
022 [Interactive Coding Exercise] BMI Calculator.mp4
023 Number Manipulation and F Strings in Python.mp4
024 [Interactive Coding Exercise] Life in Weeks.mp4
025 Day 2 Project_ Tip Calculator.mp4
026 You are already in the top 50_.mp4
027 Day 3 Goals_ what we will make by the end of the day.mp4
028 Control Flow with if _ else and Conditional Operators.mp4
029 [Interactive Coding Exercise] Odd or Even_ Introducing the Modulo.mp4
030 Nested if statements and elif statements.mp4
031 [Interactive Coding Exercise] BMI 2.0.mp4
032 [Interactive Coding Exercise] Leap Year.mp4
033 Multiple If Statements in Succession.mp4
034 [Interactive Coding Exercise] Pizza Order Practice.mp4
035 Logical Operators.mp4
036 [Interactive Coding Exercise] Love Calculator.mp4
037 Day 3 Project_ Treasure Island.mp4
038 Share and Show off your Project!.mp4
039 Day 4 Goals_ what we will make by the end of the day.mp4
040 Random Module.mp4
041 [Interactive Coding Exercise] Heads or Tails.mp4
042 Understanding the Offset and Appending Items to Lists.mp4
043 [Interactive Coding Exercise] Banker Roulette - Who will pay the bill_.mp4
044 IndexErrors and Working with Nested Lists.mp4
045 [Interactive Coding Exercise] Treasure Map.mp4
046 Day 4 Project_ Rock Paper Scissors.mp4
047 Programming is like going to the Gym.mp4
048 Day 5 Goals_ what we will make by the end of the day.mp4
049 Using the for loop with Python Lists.mp4
050 [Interactive Coding Exercise] Average Height.mp4
051 [Interactive Coding Exercise] High Score.mp4
052 for loops and the range() function.mp4
053 [Interactive Coding Exercise] Adding Even Numbers.mp4
054 [Interactive Coding Exercise] The FizzBuzz Job Interview Question.mp4
055 Day 5 Project_ Create a Password Generator.mp4
056 Hard Work and Perseverance beats Raw Talent Every Time.mp4
057 Day 6 Goals_ what we will make by the end of the day.mp4
058 Defining and Calling Python Functions.mp4
059 The Hurdles Loop Challenge.mp4
060 Indentation in Python.mp4
061 While Loops.mp4
062 Hurdles Challenge using While Loops.mp4
063 Jumping over Hurdles with Variable Heights.mp4
064 Final Project_ Escaping the Maze.mp4
065 Why is this _so_ Hard_! Can I really do this_.mp4
066 Day 7 Goals_ what we will make by the end of the day.mp4
067 How to break a Complex Problem down into a Flow Chart.mp4
068 Challenge 1 - Picking a Random Words and Checking Answers.mp4
069 Challenge 1 Solution - How to Check the User's Answer.mp4
070 Challenge 2 - Replacing Blanks with Guesses.mp4
071 Challenge 2 Solution - How to Replace the Blanks.mp4
072 Challenge 3 - Checking if the Player has Won.mp4
073 Challenge 3 Solution - How to Check if the Player Won.mp4
074 Challenge 4 - Keeping Track of the Player's Lives.mp4
075 Challenge 4 Solution - How to Keep Track of the Player's Lives.mp4
076 Challenge 5 - Improving the User Experience.mp4
077 Challenge 5 Solution - How to Add ASCII Art and Improve the UI.mp4
078 The Benefits of Daily Practice.mp4
079 Day 8 Goals_ what we will make by the end of the day.mp4
080 Functions with Inputs.mp4
081 Positional vs. Keyword Arguments.mp4
082 [Interactive Coding Exercise] Paint Area Calculator.mp4
083 [Interactive Coding Exercise] Prime Number Checker.mp4
084 Caesar Cipher Part 1 - Encryption.mp4
085 Caesar Cipher Part 2 - Decryption.mp4
086 Caesar Cipher Part 3 - Reorganising our Code.mp4
087 Caesar Cipher Part 4 - User Experience Improvements & Final Touches.mp4
088 How You Can _Stay_ Motivated.mp4
089 Day 9 Goals_ what we will make by the end of the day.mp4
090 The Python Dictionary_ Deep Dive.mp4
091 [Interactive Coding Exercise] Grading Program.mp4
092 Nesting Lists and Dictionaries.mp4
093 [Interactive Coding Exercise] Dictionary in List.mp4
094 The Secret Auction Program Instructions and Flow Chart.mp4
095 Solution and Complete Code for the Secret Auction Program.mp4
096 Motivation and the Accountability Trick.mp4
097 Day 10 Goals_ what we will make by the end of the day.mp4
098 Functions with Outputs.mp4
099 Multiple return values.mp4
100 [Interactive Coding Exercise] Days in Month.mp4
101 Docstrings.mp4
102 Calculator Part 1_ Combining Dictionaries and Functions.mp4
103 Print vs. Return.mp4
104 While Loops, Flags and Recursion.mp4
105 Calculator Finishing Touches and Bug Fixes.mp4
106 How to Get a Good Night's Sleep.mp4
107 Day 11 Goals_ what we will make by the end of the day.mp4
108 Blackjack Program Requirements and Game Rules.mp4
109 Hint 4 & 5 Solution Walkthrough.mp4
110 Hint 6-8 Solution Walkthrough.mp4
111 Hint 9 Solution Walkthrough_ Refactoring and calling calculate_score().mp4
112 Hint 10-12 Solution Walkthrough.mp4
113 Hint 13 Solution Walkthrough.mp4
114 A Solid Foundation goes a Long Way.mp4
115 Namespaces_ Local vs. Global Scope.mp4
116 Does Python Have Block Scope_.mp4
117 How to Modify a Global Variable.mp4
118 Python Constants and Global Scope.mp4
119 Introducing the Final Project_ The Number Guessing Game.mp4
120 Solution & Walkthrough to the Number Guessing Game.mp4
121 Don't be too hard on yourself.mp4
122 Describe the Problem.mp4
123 Reproduce the Bug.mp4
124 Play Computer and Evaluate Each Line.mp4
125 Fixing Errors and Watching for Red Underlines.mp4
126 Squash bugs with a print() Statement.mp4
127 Bringing out the BIG Gun_ Using a Debugger.mp4
128 Final Debugging Tips.mp4
129 [Interactive Coding Exercise] Debugging Odd or Even.mp4
130 [Interactive Coding Exercise] Debugging Leap Year.mp4
131 [Interactive Coding Exercise] Debugging FizzBuzz.mp4
132 Building Confidence.mp4
133 Introduction & Program Requirements for the Higher Lower Game.mp4
134 Solution & Walkthrough of the Higher Lower Game.mp4
135 Study Tip_ Set Reminders in Your Calendar to Review.mp4
136 Installing Python Locally on Your Computer.mp4
137 Download PyCharm for Windows or Mac.mp4
138 PyCharm's Charming Features (while you wait for the download to finish).mp4
139 How to Install PyCharm on Windows.mp4
140 Installing PyCharm on Mac.mp4
141 Introduction & Requirements for the Coffee Machine Project.mp4
142 Solution & Walkthrough for the Coffee Machine Code.mp4
143 Location, Location, Location - Pavlov's Coding Corner.mp4
144 Why do we need OOP and how does it work_.mp4
145 How to use OOP_ Classes and Objects.mp4
146 Constructing Objects and Accessing their Attributes and Methods.mp4
147 How to Add Python Packages and use PyPi.mp4
148 Practice Modifying Object Attributes and Calling Methods.mp4
149 Building the Coffee Machine in OOP.mp4
150 Walkthrough and Solution for the OOP Coffee Machine.mp4
151 Don't forget to review occasionally.mp4
152 Day 17 Goals_ what we will make by the end of the day.mp4
153 How to create your own Class in Python.mp4
154 Working with Attributes, Class Constructors and the __init__() Function.mp4
155 Adding Methods to a Class.mp4
156 Quiz Project Part 1_ Creating the Question Class.mp4
157 Quiz Project Part 2_ Creating the List of Question Objects from the Data.mp4
158 Quiz Project Part 3_ The QuizBrain and the next_question() Method.mp4
159 Quiz Project Part 4_ How to continue showing new Questions.mp4
160 Quiz Project Part 5_ Checking Answers and Keeping Score.mp4
161 The Benefits of OOP_ Use Open Trivia DB to Get New Questions.mp4
162 Run for that Bus!.mp4
163 Day 18 Goals_ what we will make by the end of the day.mp4
164 Understanding Turtle Graphics and How to use the Documentation.mp4
165 Turtle Challenge 1 - Draw a Square.mp4
166 Importing Modules, Installing Packages, and Working with Aliases.mp4
167 Turtle Challenge 2 - Draw a Dashed Line.mp4
168 Turtle Challenge 3 - Drawing Different Shapes.mp4
169 Turtle Challenge 4 - Generate a Random Walk.mp4
170 Python Tuples and How to Generate Random RGB Colours.mp4
171 Turtle Challenge 5 - Draw a Spirograph.mp4
172 The Hirst Painting Project Part 1 - How to Extract RGB Values from Images.mp4
173 The Hirst Painting Project Part 2 - Drawing the Dots.mp4
174 Space out your study sessions and stay consistent.mp4
175 Day 19 Goals_ what we will make by the end of the day.mp4
176 Python Higher Order Functions & Event Listeners.mp4
177 Challenge_ Make an Etch-A-Sketch App.mp4
178 Object State and Instances.mp4
179 Understanding the Turtle Coordinate System.mp4
180 Aaaand, we're off to the races!.mp4
181 Expand on the Solutions.mp4
182 Day 20 Goals_ what we will make by the end of the day.mp4
183 Screen Setup and Creating a Snake Body.mp4
184 Animating the Snake Segments on Screen.mp4
185 Create a Snake Class & Move to OOP.mp4
186 How to Control the Snake with a Keypress.mp4
187 Programming is not Memorising.mp4
188 Day 21 Goals_ what we will make by the end of the day.mp4
189 Class Inheritance.mp4
190 Detect Collisions with Food.mp4
191 Create a Scoreboard and Keep Score.mp4
192 Detect Collisions with the Wall.mp4
193 Detect Collisions with your own Tail.mp4
194 How to Slice Lists & Tuples in Python.mp4
195 Stay motivated by remembering the reason you signed up.mp4
196 Day 22 Goals_ what you will make by the end of the day.mp4
197 Set up the Main Screen.mp4
198 Create a Paddle that responds to Key Presses.mp4
199 Write the Paddle Class and Create the Second Paddle.mp4
200 Write the Ball Class and Make the Ball Move.mp4
201 Add the Ball Bouncing Logic.mp4
202 How to Detect Collisions with the Paddle.mp4
203 How to Detect when the Ball goes Out of Bounds.mp4
204 Score Keeping and Changing the Ball Speed.mp4
205 Picturing fears_ even the worst-case scenario is not so scary.mp4
206 Day 23 Goals_ what you will make by the end of the day.mp4
208 How to use the Starter Code.mp4
211 Solution to Step 3 - Create the Player Behaviour.mp4
212 Solution to Step 4 - Create the Car Behaviour.mp4
213 Solution to Step 5 - Detect when the Turtle collides with a Car _squish_.mp4
214 Solution to Step 6 - Detect when the Player has reached the other side.mp4
215 Solution to Step 7 - Add the Scoreboard and Game Over sequence.mp4
216 This course is not about typing out code.mp4
217 Day 24 Goals_ what you will make by the end of the day.mp4
218 Add a High Score to the Snake Game.mp4
219 How to Open, Read, and Write to Files using the _with_ Keyword.mp4
220 Challenge_ Read and Write the High Score to a File in Snake.mp4
221 Understand Relative and Absolute File Paths.mp4
222 Introducing the Mail Merge Challenge.mp4
223 Solution & Walkthrough for the Mail Merge Project.mp4
224 What's the correct solution_ What's the best answer_ What's the right way_.mp4
225 Day 25 Goals_ what we will make by the end of the day.mp4
226 Reading CSV Data in Python.mp4
227 DataFrames & Series_ Working with Rows & Columns.mp4
228 The Great Squirrel Census Data Analysis (with Pandas!).mp4
229 U.S. States Game Part 1_ Setup.mp4
230 U.S. States Game Part 2_ Challenge with .csv.mp4
231 U.S. States Game Part 3_ Saving Data to .csv.mp4
232 Day 26 Goals_ what you will make by the end of the day.mp4
233 How to Create Lists using List Comprehension.mp4
234 [Interactive Coding Exercise] Squaring Numbers.mp4
235 [Interactive Coding Exercise] Filtering Even Numbers.mp4
236 [Interactive Coding Exercise] Data Overlap.mp4
237 Apply List Comprehension to the U.S. States Game.mp4
238 How to use Dictionary Comprehension.mp4
239 [Interactive Coding Exercise] Dictionary Comprehension 1.mp4
240 [Interactive Coding Exercise] Dictionary Comprehension 2.mp4
241 How to Iterate over a Pandas DataFrame.mp4
242 Introducing the NATO Alphabet Project.mp4
243 Solution & Walkthrough for the NATO Alphabet Project.mp4
244 Day 27 Goals_ what we will make by the end of the day.mp4
245 History of GUI and Introduction to Tkinter.mp4
246 Creating Windows and Labels with Tkinter.mp4
247 Setting Default Values for Optional Arguments inside a Function Header.mp4
248 _args_ Many Positional Arguments.mp4
249 __kwargs_ Many Keyword Arguments.mp4
250 Buttons, Entry, and Setting Component Options.mp4
251 Other Tkinter Widgets_ Radiobuttons, Scales, Checkbuttons and more.mp4
252 Tkinter Layout Managers_ pack(), place() and grid().mp4
253 Mile to Kilometers Converter Project.mp4
254 Day 28 Goals_ what we will make by the end of the day.mp4
255 How to work with the Canvas Widget and Add Images to Tkinter.mp4
256 Challenge - Complete the Application's User Interface (UI).mp4
257 Add a Count Down Mechanism.mp4
258 Dynamic Typing Explained.mp4
259 Setting Different Timer Sessions and Values.mp4
260 Adding Checkmarks and Resetting the Application.mp4
261 Day 29 Goals_ what we will make by the end of the day.mp4
262 Challenge 1 - Working with Images and Setting up the Canvas.mp4
263 Challenge 2 - Use grid() and columnspan to Complete the User Interface.mp4
264 Solution to the Creating the Grid Layout.mp4
265 Challenge 3 - Saving Data to File.mp4
266 Dialog Boxes and Pop-Ups in Tkinter.mp4
267 Generate a Password & Copy it to the Clipboard.mp4
268 Day 30 Goals_ what you will make by the end of the day.mp4
269 Catching Exceptions_ The try catch except finally Pattern.mp4
270 Raising your own Exceptions.mp4
271 [Interactive Coding Exercise] IndexError Handling.mp4
272 [Interactive Coding Exercise] KeyError Handling.mp4
273 Code Exercise_ Exception Handling in the NATO Phonetic Alphabet Project.mp4
274 Write, read and update JSON data in the Password Manager.mp4
275 Challenge 1 - Handling Exceptions in the Password Manager.mp4
276 Challenge 2 - Search for a Website in the Password Manager.mp4
277 Day 31 Goals_ what you will make by the end of the day.mp4
279 Solution & Walkthrough for Creating the UI.mp4
281 Solution & Walkthrough for Creating New Flash Cards.mp4
283 Solution & Walkthrough for Flipping Cards.mp4
285 Solution & Walkthrough for Saving Progress.mp4
286 Day 32 Goals_ what we will make by the end of the day.mp4
288 How to Send Emails with Python using SMTP.mp4
289 Working with the datetime Module.mp4
290 Challenge 1 - Send Motivational Quotes on Mondays via Email.mp4
291 Automated Birthday Wisher Project Challenge.mp4
292 Solution & Walkthrough for the Automated Birthday Wisher.mp4
293 Run Your Python Code in the Cloud!.mp4
294 Day 33 Goals_ what you will make by the end of the day.mp4
295 What are Application Programming Interfaces (APIs)_.mp4
296 API Endpoints and Making API Calls.mp4
297 Working with Responses_ HTTP Codes, Exceptions & JSON Data.mp4
298 Challenge - Build a Kanye Quotes App using the Kanye Rest API.mp4
299 Understand API Parameters_ Match Sunset Times with the Current Time.mp4
300 ISS Overhead Notifier Project - Challenge & Solution.mp4
301 Day 34 Goals_ what you will make by the end of the day.mp4
302 Trivia Question API Challenge.mp4
303 Solution & Walkthrough for getting Trivia Questions.mp4
304 Unescaping HTML Entities.mp4
305 Class based Tkinter UI.mp4
306 Python Typing & Showing the Next Question in the GUI.mp4
307 Python Typing_ Type Hints and Arrows -_.mp4
308 Check the Answer.mp4
309 Give Feedback to the Player, Keep Score and Fix the Bugs =).mp4
310 Day 35 Goals_ what you will make by the end of the day.mp4
311 What is API Authentication and Why Do We Need to Authenticate Ourselves_.mp4
312 Using API Keys to Authenticate and Get the Weather from OpenWeatherMap.mp4
313 Challenge - Check if it Will Rain in the Next 12 Hours.mp4
314 Sending SMS via the Twilio API.mp4
315 Use PythonAnywhere to Automate the Python Script.mp4
316 Understanding Environment Variables and Hiding API Keys.mp4
317 Day 36 Goals_ what you will make by the end of the day.mp4
319 Solution & Walkthrough for Step 1 - Check for Stock Price Movements.mp4
320 Solution & Walkthrough for Step 2 - Get the News Articles.mp4
321 Solution & Walkthrough for Step 3 - Send the SMS Messages.mp4
322 Day 37 Goals_ what you will make by the end of the day.mp4
323 HTTP Post Requests.mp4
324 Advanced Authentication using an HTTP Header.mp4
325 Challenge_ Add a Pixel to the Habit Tracker using a Post Request.mp4
326 Autofilling today's date using strftime.mp4
327 How to use HTTP Put and Delete Requests.mp4
328 Day 38 Goals_ what you will make by the end of the day.mp4
335 Day 39 Goals_ what you will make by the end of the day.mp4
341 Day 40 Goals_ what you will make by the end of the day.mp4
```