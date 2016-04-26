#!/usr/bin/env bash

# Automatic bash script to merge the latest changes from OpenRCT2/Localisation
# into OpenRCT2/OpenRCT2.

echo "Merge Localisation into OpenRCT2."

# Clone repositories
echo "Cloning repositories."
git clone -b master git@github.com:OpenRCT2/Localisation.git Localisation
git clone -b develop git@github.com:OpenRCT2/OpenRCT2.git OpenRCT2

# Copy over language files
echo "Copying language files"
for f in ./Localisation/data/language/*
do
    filename=$(basename $f)
    cp $f "./OpenRCT2/data/language/$filename"
done

# Commit and push
pushd ./OpenRCT2
if [[ $(git status -s) ]]; then
    echo "Committing and pushing..."
    git add .
    git commit -m "Merge Localisation/master into OpenRCT2/develop."
    git push
    echo "Complete"
else
    echo "No changes to merge."
fi
popd

# Remove files
rm -rf ./OpenRCT2
rm -rf ./Localisation
