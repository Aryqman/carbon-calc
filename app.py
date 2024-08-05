import streamlit as st

#reference: greenhouse gas protocol or ghgprotocol.org
emission_factors = {
    "India": {
        "transport" : 0.14, #in kgCO2 per km
        "power" : 0.82, #in kgCO2 per kWh
        "wastes" : 0.1, #in kgCO2 per kg
        "food" : 1.25, #in kgCO2 per meal

    }
}

#streamlit configurations
st.set_page_config(layout="wide", page_title="Personal Carbon Calculator")
st.title("🌍 Carbon Footprint Calculator")


#inputs
st.subheader("Your country")
country = st.selectbox("Select", ["India"])

colA, colB = st.columns(2)
with colA:
    st.subheader("Daily travel distance(in km)")
    distance = st.slider("Distance", 0.0, 50.0, key="distance_input")
    st.subheader("Monthly power consumption(in kWh)")
    electricity = st.slider("Electricity", 0.0, 500.0, key="power_input")

with colB:
    st.subheader("Weekly waste generation(in kg)")
    waste = st.slider("Waste", 0.0, 100.0, key="waste_input")
    st.subheader("Number of meals per day")
    food = st.slider("Meals", 0.0, 10.0, key="meal_input")

#converting inputs to yearly values
if distance > 0:
    distance = distance * 365
if electricity > 0:
    electricity = electricity * 12 #cus monthly
if waste > 0:
    waste= waste * 52 #cus weekly
if food > 0:
    food = food * 365

#calculation of emissions
transport_emissions = emission_factors[country]["transport"] * distance
electric_emissions = emission_factors[country]["power"] * electricity
diet_emissions = emission_factors[country]["food"] * food
waste_emissions = emission_factors[country]["wastes"] * waste

transport_emissions = round(transport_emissions/1000, 2)
electric_emissions = round(electric_emissions/1000,2)
diet_emissions = round(diet_emissions/1000,2)
waste_emissions = round(waste_emissions/1000,2)


total_emissions = round(
    transport_emissions + diet_emissions + waste_emissions + electric_emissions,2
)

if st.button("Calculate CO2 Emissions"):
    st.header("Results")
    colC, colD = st.columns(2)
    
    with colC:
        st.subheader("Carbon Emissions by Category")
        st.info(f"🚗 Transportation: {transport_emissions} tonnes CO2 per year")
        st.info(f"💡 Electricity: {electric_emissions} tonnes CO2 per year")
        st.info(f"🍽️ Diet: {diet_emissions} tonnes CO2 per year")
        st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")

    with colD:
        st.subheader("Total Carbon Footprint")
        st.success(f"Your total carbon footprint is {total_emissions} tonnes C02 per year")
        st.warning("In  2023, the per capita C02 emissions for India was 2.0 tons.")
