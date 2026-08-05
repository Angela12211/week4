// void main(){
//     int score = 85;

//     if (score >= 75){
//         print('passed');
//     } else {
//         print('failed');
//     }
//     for(int i =1; i <=3; i++) {
//         print('count: $i');
//     }
// }




// 1)

// import 'dart:io';

// void main() {
  
//   stdout.write('Enter a number: ');
//   String? input = stdin.readLineSync();

//   if (input != null) {
   
//     int? number = int.tryParse(input);

//     if (number != null) {
      
//       if (number > 0) {
//         print('$number is positive');
////       } else if (number < 0) {
//         print('$number is negative');
//       } else {
//         print('the number is zero');
//       }
//     } else {
//       print('Invalid input! Please enter a valid number.');
//     }
//   }
// }

// bmc

// import 'dart:io';

// // Function to compute the average score
// double computeAverage(List<double> scores) {
//   double total = 0;

//   for (double score in scores) {
//     total += score;
//   }

//   return total / scores.length;
// }

// void main() {
//   // Ask for student's name
//   stdout.write("Enter student name: ");
//   String name = stdin.readLineSync()!;

//   // Ask for age
//   stdout.write("Enter age: ");
//   int age = int.parse(stdin.readLineSync()!);

//   // List to store quiz scores
//   List<double> scores = [];

//   // Ask for three quiz scores
//   for (int i = 1; i <= 3; i++) {
//     stdout.write("Enter quiz $i: ");
//     double score = double.parse(stdin.readLineSync()!);
//     scores.add(score);
//   }

//   // Compute average using function
//   double average = computeAverage(scores);

//   // Determine status and remark
//   String status;
//   String remark;

//   if (average >= 75) {
//     status = "Passed";
//     remark = "Good job, keep it up!";
//   } else {
//     status = "Failed";
//     remark = "Study harder next time.";
//   }

//   // Display result
//   print("\nStudent Name: $name");
//   print("Age: $age");
//   print("Average: ${average.toStringAsFixed(2)}");
//   print("Status: $status");
//   print("Remark: $remark");
// }












// int add(int a, int b) {
//     return a + b;
// }

// void main(){
//     print(add(4,6));
// }

// void main(){
//     List<String> fruits = ['Apple', 'Banana', 'Mango'];
//     Set<int> numbers = {1,2,3,4,5};
//     Map<String, int> grades = {'math' : 90, 'Science' : 95};

//     print(fruits[0]);
//     print(numbers);
//     print(grades['math']);

// }



// 2
// void main(){

// Map<String, String> name ={'Sairon':'Binuya', 'Jasmin':'Santos', 'Aiko':'Awas', 'Julius':'Arcega', 'Kan':'Cozy', 'Niki':'Zefanya'};


// print(name['Sairon']);
// print(name['Jasmin']);
// print(name['Aiko']);
// print(name['Julius']);
// print(name['Kan']);
// print(name['Niki']);
// }


// class Students {
//     String name;
//     int age;

//     Students(this.name, this.age );

//     void introduce () {
//         print('My name is $name and I am $age years old' );
//     }
// }

// void main(){
//     Students s1 = Students('Ana',18);
//     s1.introduce();
// }






// 3

// class Cars {
//     String brand;
//     int year;

//     Cars(this.brand, this.year);


//     void introduce () {
//        print('Brand $brand and Year $year');
//     }

// }

// void main(){
//     Cars s1 = Cars('BMW', 1999);
//     s1.introduce();

//     Cars s2 = Cars('Toyota', 1899);
//     s2.introduce();


// }



// class Animal {
//     void eat() {
//         print('Eating...');
//     }
// }

// class Dog extends Animal {
//     void bark() {
//         print('Bark!');
//     }
// }

// void main() {
//     Dog dog = Dog();
//     dog.eat();
//     dog.bark();
// }





// // 4
// class Animal {
//     void fly() {
//         print('Flying......');
//     }
// }

// class Bird extends Animal {
//     void tweet() {
//         print('twee3333eeteeEEEeeeet!');
//     }
// }

// void main() {

//     Bird bird = Bird();
//     bird.fly();
//     bird.tweet();
// }

