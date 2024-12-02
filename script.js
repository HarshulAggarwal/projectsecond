const searchBtn = document.getElementById("search-btn");
const mealList = document.getElementById("meal");
const mealDetailsContent = document.querySelector(".meal-details-content");
const recipeCloseBtn = document.getElementById("recipe-close-btn");
const searchBtnIngredient = document.getElementById("search-btn-ingredient");

// event listeners
searchBtn.addEventListener("click", () => getMealList("i"));
searchBtnIngredient.addEventListener("click", () => getMealList("a"));
mealList.addEventListener("click", getMealRecipe);
recipeCloseBtn.addEventListener("click", () => {
  mealDetailsContent.parentElement.classList.remove("showRecipe");
});
