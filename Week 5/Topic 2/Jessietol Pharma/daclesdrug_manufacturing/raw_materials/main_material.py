def main():
    from raw_materials.quality import check_quality
    from raw_materials.recipe import generate_recipe
    from raw_materials.supplier import inventory_report


    check_quality()
    generate_recipe()
    inventory_report()
    print("\n")

