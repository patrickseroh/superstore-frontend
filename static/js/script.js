const subCategoryMap = {
    "Furniture": ["Furnishings", "Tables", "Bookcases", "Chairs"],
    "Office Supplies": ["Binders", "Fasteners", "Supplies", "Envelopes", "Appliances", "Labels", "Art", "Paper", "Storage"],
    "Technology": ["Accessories", "Phones", "Copiers", "Machines"]
};

const regionMap = {
    "US": ["Central", "East", "South", "West"],
    "LATAM": ["Caribbean", "Central", "North", "South"],
    "APAC": ["Central Asia", "North Asia", "Oceania", "Southeast Asia"],
    "EU": ["Central", "North", "South"],
    "Africa": ["Africa"],
    "Canada": ["Canada"],
    "EMEA": ["EMEA"]
};

document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.toggle-btn');
    const sections = document.querySelectorAll('.tab-content');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            buttons.forEach(btn => btn.classList.remove('active'));
            sections.forEach(section => section.classList.remove('active'));

            button.classList.add('active');
            const targetId = button.getAttribute('data-target');
            document.getElementById(targetId).classList.add('active');
        });
    });

    function setupDependentDropdown(parentSelectId, childSelectId, mapping) {
        const parentSelect = document.getElementById(parentSelectId);
        const childSelect = document.getElementById(childSelectId);

        function updateChildOptions() {
            const selectedParent = parentSelect.value;
            const options = mapping[selectedParent] || [];

            childSelect.innerHTML = "";
            options.forEach(opt => {
                const el = document.createElement("option");
                el.value = opt;
                el.textContent = opt;
                childSelect.appendChild(el);
            });
        }

        parentSelect.addEventListener("change", updateChildOptions);
        updateChildOptions();
    }

    setupDependentDropdown("category-sales", "sub_category-sales", subCategoryMap);
    setupDependentDropdown("category-profit", "sub_category-profit", subCategoryMap);
    setupDependentDropdown("market-sales", "region-sales", regionMap);
    setupDependentDropdown("market-profit", "region-profit", regionMap)
});

