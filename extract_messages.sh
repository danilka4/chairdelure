if [ ! -f "data/package.zip" ]; then
    echo "Name your file package.zip inside the data folder"
    exit 1
fi

if [ ${#} -lt 1 ]; then
    echo "Please list an output csv"
    exit 1
fi

cd data

echo "ID,Timestamp,Contents,Attachments" > $1

unzip package.zip


if [[ "$OSTYPE" == "darwin"* ]]; then
    cat package/messages/*/messages.csv | grep -v ID,Timestamp,Contents,Attachments >> $1

    rm -rf package/
    rm -rf __MACOSX/
else
    cat messages/*/messages.csv | grep -v ID,Timestamp,Contents,Attachments >> $1

    rm -rf account
    rm -rf activities_e
    rm -rf activities_w
    rm -rf activity
    rm -rf messages
    rm -rf programs
    rm -rf servers
    rm README.txt
fi

cd ..
