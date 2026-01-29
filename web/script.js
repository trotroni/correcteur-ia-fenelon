function corriger() {
    const texte = document.getElementById("copie").value;

    fetch("/corriger", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({copie: texte})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("resultat").textContent =
            "Note : " + data.note + "/20\n\n" +
            JSON.stringify(data.details, null, 2);
    });
}
