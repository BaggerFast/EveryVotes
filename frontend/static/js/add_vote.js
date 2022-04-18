let addVote = document.getElementById("addVoteVariantBtn")
let voteVariant = document.getElementById("voteVariantInput")
let postVoteVariants = document.getElementById("post_vote_variants")

addVote.addEventListener("click", function () {
  if (voteVariant.value === "" )
    return
    let voteList = document.getElementById('voteVariantsList')
    let voteLi = document.createElement("li");
    voteLi.appendChild(document.createTextNode(voteVariant.value));
    voteList.appendChild(voteLi);
    postVoteVariants.append(new Option(voteVariant.value, voteVariant.value, true, true))
    voteVariant.value = ''

});
