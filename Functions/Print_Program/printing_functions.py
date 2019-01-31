#Module for Print_Program

#Functions
def print_models(unprintedDesigns, compModels):
    """
    Simulates printing each design until none are left
    Moves each design to compModels list once done
    """
    while unprintedDesigns:
        currentDesign = unprintedDesigns.pop()

        # Simulate creating a 3D print from design
        print("Printing model: " + currentDesign)
        compModels.append(currentDesign)


def show_completed_models(compModels):
    """Show all models that were printed"""
    print("\nThe following models have been printed:")
    for compModel in compModels:
        print(compModel)
