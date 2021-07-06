#!/bin/bash


printf " \n\e[32m \e[1mChecking for PEP8 compliance...\e[0m\n"

echo "PATH=$PATH:/home/gitlab-runner/.local/bin" >> .bashrc
source .bashrc

for file in $(find . -name "*.py")
do
    if [[ ${file: -3} == ".py" ]]
    then 
        echo $file | tr -d '\n'
        if [[ $(pycodestyle $file) ]]
        then
            printf ".....\e[31m \e[1mcheck:\e[0m\n"
            pycodestyle $file
        else
            printf ".....\e[32m \e[1mok!\e[0m\n"
        fi
    fi
done

printf "\e[32m \e[1mPEP8 check done.\e[0m\n \n "
