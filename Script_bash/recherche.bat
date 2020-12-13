champs="Bactérie"
for champ in $champs
do
    echo importation de $champ
    curl "https://fr.wikipedia.org/w/index.php?title=${champ}&action=raw" > ../PAGES/$champ
done