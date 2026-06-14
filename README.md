# ML_hw_04_Facial-Expression-Recognition-Challenge
Challenges in Representation Learning: Facial Expression Recognition Challenge

--- 
## კონკურსის მიმოხილვა
კონკურსის მიზანია ადამინაის სახის გამოსახულებიდან 7 სავარაუდო ემოციის ამოცნობა. train.csv შეიცავდა 2 სვეტს, ემოციებისას- რომელიც შეიცავს ნულიდან ექვსამდე მნიშნელობებს (0=Angry, 1=Disgust, 2=Fear, 3=Happy, 4=Sad, 5=Surprise, 6=Neutral), და პიქსელების სტრინგს. ეს ამოცანა ფასდება accuracy-ს მიხედვით. 

---
## რეპოზიტორიის სტრუქტურა

---
## მონაცემების დამუშვება (Setup & EDA)
გადავწყვიტე რომ ცალკე ნოუთბუქში მქონდეს setup და ასევე  data understanding, რასაც შემდეგ ყველა სხვა ნოუთბუქში გამოვიყენებ. ყოველი ახალი ნოუთბუქი იქნება ახალი არქიტექტურისთვის. ამ ამოცანი ერთ-ერთ მთავარი გამოწვევა არის  დაუბალანსებელი დატა
<img width="1532" height="962" alt="Screenshot 2026-06-14 123936" src="https://github.com/user-attachments/assets/71cdc532-a9d8-4039-a308-fb84610f883f" />
<img width="2172" height="314" alt="image" src="https://github.com/user-attachments/assets/845fa871-1b2e-43d8-a7cb-7456d26141dc" />
ასეთი საოცარი ემოციები გვაქ.
აქაც ცხადია train დატა დავსპლიტე train-ად და validation-ად. Train:  (25838, 2) Val:  (2871, 2)
თავიდან train.csv-ის (28,709 sample) დაყოფას ვაკეთებდით 2 ნაწილად — train (90%) და validation (10%), stratified split-ით. თუმცა, რადგან validation set-ს ვიყენებდით ერთდროულად ორი მიზნით — training-ის დროს overfitting-ის მონიტორინგისთვის და სხვადასხვა architecture-ისა და hyperparameter-ის შედარებისთვის — გადავწყვიტეთ დაყოფა 3 ნაწილად გადაგვეკეთებინა: train (70%), validation (15%), test (15%), stratified split-ით ემოციების ბალანსის შესაბამისად.
ამ ცვლილების მიზანი: validation set გამოვიყენებთ training-ის მონიტორინგისა და architecture/hyperparameter-ის შერჩევისთვის, ხოლო test set დარჩება სრულად "უცნობი" — მას გამოვიყენებთ მხოლოდ ერთხელ, საუკეთესო model-ზე, საბოლოო, მიუკერძოებელი accuracy-ის გამოსათვლელად. ეს გვაშორებს იმ რისკს, რომ ჩვენი საბოლოო შედეგები იყოს ოპტიმისტურად "მორგებული" validation set-ზე, რომელზეც decision-making-ი მოხდა. გამოვიყენე stratified splitting, რადგან თანაბრად ყოფილიყო ემოციის გადანაწილება საბსეტებში და მოდელს შეძლებოდა განზოგადება და თითოეული ემოციის სწორად დასწავლა. შემდეგ გავუკეთე ნორმალიზაცია, ანუ პიქსელების მნიშვნელობები [0, 255] გადავიყვანე [0, 1]-ში.




