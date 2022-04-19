function variantInnerHTML(variant_text) {
    return variant_text + '<div class="deleteMe">Delete</div>';
}


let voteVariant = document.getElementById("voteVariantInput")
let voteVariantsSelector = document.getElementById("post_vote_variants")

document.getElementById("addVoteVariantBtn").addEventListener("click", function () {
  if (voteVariant.value === "" )
    return
  let voteList = document.getElementById('voteVariantsList')
  let voteLi = document.createElement("li");
  voteLi.innerHTML = variantInnerHTML(voteVariant.value)
  voteList.appendChild(voteLi);
  voteVariantsSelector.append(new Option(voteVariant.value, voteVariant.value, true, true))
  voteVariant.value = ''
});
