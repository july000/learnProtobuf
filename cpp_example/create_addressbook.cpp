#include "addressbook.pb.h"
#include <fstream>
#include <iostream>

void createAddressBook(){
  tutorial::AddressBook addressbook;

  tutorial::Person* person1 = addressbook.add_people();
  person1->set_name("John");
  person1->set_id(123);
  person1->set_email("john@example.com");

  tutorial::Person::PhoneNumber* phone1 = person1->add_phones();
  phone1->set_number("123456789");
  phone1->set_type(tutorial::Person_PhoneType::Person_PhoneType_PHONE_TYPE_MOBILE);

  tutorial::Person* person2 = addressbook.add_people();
  person2->set_name("Jane");
  person2->set_id(456);
  person2->set_email("jane@example.com");

  tutorial::Person::PhoneNumber* phone2 = person2->add_phones();
  phone2->set_number("987654321");
  phone2->set_type(tutorial::Person_PhoneType::Person_PhoneType_PHONE_TYPE_HOME);

  std::ofstream output("./addressbook.pb", std::ios::binary);
  if(addressbook.SerializeToOstream(&output)){
    std::cout<<"addressbook write file success"<<std::endl;
  }
  else{
    std::cout<<"addressbook write file failed"<<std::endl;
  }
  output.close();
}

int main(){
  // createAddressBook();
  std::cout<<"hello world"<<std::endl;
  return 0;
}