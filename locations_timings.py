locations_timings = [
    ("skating_lot", "skating_rink", 30),
    ("skating_rink", "bsc", 30),
    ("path_fields_side", "becc", 120),
    ("path_fields_bryant", "macdowell_field", 45),
    ("path_fields_bryant", "hartwell_rogers_field", 45),
    ("path_fields_seating", "macdowell_field", 45),
    ("path_fields_seating", "hartwell_rogers_field", 45),
    ("path_fields_seating", "isbrandtsen_field", 45),
    ("path_fields_seating", "softball_field", 45),
    ("path_fields_seating", "path_fields_bryant", 60),
    ("path_fields_seating", "path_vw_hill_top", 60),
    ("path_vw_hill_top", "isbrandtsen_field", 45),
    ("path_vw_hill_top", "softball_field", 45),
    ("path_fields_side", "path_vw_hill_top", 45),
    ("path_fields_side", "tennis_court", 45),
    ("path_vw_hill_top", "van_winkle", 30),
    ("tennis_court", "coleman_lot", 60),
    ("coleman_lot", "van_winkle", 45),
    ("path_vw_hill_top", "coleman", 45),
    ("van_winkle", "coleman", 30),
    ("coleman", "path_map_hill_1", 30),
    ("van_winkle", "path_map_hill_1", 75),
    ("coleman_lot", "coleman", 60),
    ("coleman_lot", "path_map_hill_1", 45),
    ("path_map_hill_1", "path_map_hill_2", 75),
    ("coleman_lot", "path_map_hill_2", 60),
    ("path_map_hill_1", "path_pietz_mccullough", 60),
    ("path_vw_hill_top", "path_vw_hill_bottom", 120),
    ("path_pietz_mccullough", "mccullough", 45),
    ("mccullough", "path_map_hill_2", 60),
    ("mccullough", "putney", 45),
    ("putney", "mandell", 45),
    ("path_map_hill_2", "path_map_hill_3", 120),
    ("mandell", "path_map_hill_3", 90),
    ("path_map_hill_3", "trim_lot", 45),
    ("path_map_hill_3", "foundry", 30),
    ("foundry", "foundry_lot", 30),
    ("foundry_lot", "hollister_lot", 30),
    ("path_map_hill_3", "path_map_hill_4", 75),
    ("foundry_lot", "path_keith_canfield", 90),
    ("path_keith_canfield", "keith", 15),
    ("path_keith_canfield", "canfield", 15),
    ("path_keith_canfield", "pietz", 30),
    ("path_keith_canfield", "path_pietz_mccullough", 45),
    ("path_pietz_mccullough", "keith", 45),
    ("path_pietz_mccullough", "pietz", 30),
    ("path_vw_hill_bottom", "chapel", 30),
    ("chapel", "kriebel", 30),
    ("chapel", "sorenson", 45),
    ("sorenson", "reynolds", 15),
    ("sorenson", "path_vw_hill_bottom", 30),
    ("canfield", "reynolds", 30),
    ("path_reynolds_canfield", "canfield", 30),
    ("path_reynolds_canfield", "reynolds", 30),
    ("path_reynolds_canfield", "hollister_lot", 30),
    ("hollister_lot", "path_map_hill_4", 15),
    ("hollister", "path_map_hill_4", 15),
    ("path_map_hill_4", "trim", 30),
    ("trim", "rogers", 30),
    ("path_sullivan", "rogers", 60),
    ("path_sullivan", "forest", 15),
    ("path_sullivan", "public_safety", 15),
    ("public_safety", "sullivan", 30),
    ("sullivan", "sullivan_lot", 30),
    ("sullivan", "central_services", 30),
    ("central_services", "sullivan_lot", 30),
    ("sullivan_lot", "forest_annex", 15),
    ("forest", "forest_lot", 30),
    ("forest_lot", "path_sullivan", 30),
    ("path_sullivan", "path_college_1", 30),
    ("path_college_1", "path_college_2", 60),
    ("path_college_2", "path_college_3", 45),
    ("path_college_1", "rogers", 30),
    ("path_map_hill_4", "path_college_1", 30),
    ("path_college_3", "sorenson", 15),
    ("path_college_3", "reynolds", 15),
    ("path_college_3", "globe", 15),
    ("path_college_3", "path_college_4", 60),
    ("globe", "path_manor_way_1", 15),
    ("path_college_1", "path_nichols_1", 45),
    ("path_nichols_1", "nichols_lot", 15),
    ("path_nichols_1", "path_nichols_2", 30),
    ("path_nichols_2", "nichols", 30),
    ("path_nichols_2", "cruikshank", 30),
    ("path_nichols_2", "path_manor_way_3", 30),
    ("path_manor_way_3", "cruikshank", 15),
    ("path_manor_way_3", "millea", 30),
    ("path_manor_way_3", "post_office", 45),
    ("path_manor_way_3", "manor_north", 45),
    ("path_manor_way_3", "path_manor_way_2",15 ),
    ("path_manor_way_2", "nichols", 30),
    ("path_manor_way_1", "manor_south", 15),
    ("path_manor_way_2", "manor_south", 15),
    ("path_manor_way_2", "manor_quad", 30),
    ("manor_quad", "manor_south", 30),
    ("manor_quad", "manor_north", 30),
    ("manor_quad", "manor_west", 30),
    ("manor_west", "innovation", 15),
    ("manor_quad", "manor_central", 30),
    ("manor_quad", "tomasso", 60),
    ("manor_south", "path_college_4", 30),
    ("path_college_4", "commons", 15),
    ("path_college_4", "path_college_5", 45),
    ("manor_north", "mattos", 45),
    ("mattos", "tomasso", 45),
    ("tomasso", "path_tomasso_lawn", 30),
    ("path_tomasso_lawn", "luksic", 30),
    ("path_tomasso_lawn", "blank", 30),
    ("tomasso", "path_mustard_blank", 30),
    ("path_mustard_blank", "mustard", 30),
    ("path_mustard_blank", "blank", 30),
    ("mustard", "olin_lot", 30),
    ("olin_lot", "blank", 30),
    ("blank", "luksic", 15),
    ("luksic", "olin", 45),
    ("olin_lot", "olin", 30),
    ("path_tomasso_lawn", "path_college_5", 30),
    ("kriebel", "gerber", 30),
    ("gerber", "horn", 15),
    ("horn", "horn_cpu", 30),
    ("horn", "commons", 15),
    ("horn", "babson_hall", 15),
    ("babson_hall", "babson_lot", 30),
    ("babson_lot", "path_college_5", 15),
    ("path_college_5", "path_college_6", 30),
    ("path_college_6", "path_webster_stairs", 45),
    ("path_webster_stairs", "horn_cpu", 45),
    ("path_webster_stairs", "webster", 30),
    ("path_college_6", "olin", 15),
    ("path_college_6", "path_college_7", 15),
    ("olin", "path_olin_knight", 15),
    ("path_olin_knight", "knight_lot", 45),
    ("olin", "malloy", 45),
    ("malloy", "knight", 15),
    ("malloy", "knight_lot", 30),
    ("path_college_7", "malloy", 15),
    ("path_college_7", "brac", 30),
    ("path_college_7", "path_college_8", 60),
    ("webster", "webster_lot", 30),
    ("brac", "webster_lot", 30),
    ("webster_lot", "path_fields_bryant", 30),
    ("path_fields_bryant", "becc_lot", 45),
    ("becc_lot", "woodside", 45),
    ("woodside", "woodside_lot", 30),
    ("path_college_8", "bryant", 30),
    ("bryant", "path_babson_way_1", 30),
    ("bryant", "knight_lot", 45),
    ("knight_lot", "path_babson_way_1", 45),
    ("path_babson_way_1", "westgate", 30),
    ("westgate", "bryant_lot", 45),
    ("bryant", "bryant_lot", 45),
    ("path_college_8", "path_bryant_way", 30),
    ("path_bryant_way", "path_babson_way_2", 30),
    ("path_bryant_way", "webster_lot", 30),
    ("path_college_8", "path_babson_way_2", 30),
    ("path_babson_way_2", "bryant_lot", 30),
    ("woodside_lot", "path_babson_way_2", 30),
    ("path_babson_way_2", "path_babson_way_3", 120),
    ("path_babson_way_3", "woodland_lot", 30),
    ("path_babson_way_3", "woodland_1", 30),
    ("path_babson_way_3", "woodland_9", 15),
    ("woodland_1", "woodland_2", 30),
    ("woodland_2", "woodland_2a", 30),
    ("woodland_2a", "woodland_10", 30),
    ("woodland_10", "woodland_9", 15),
    ("woodland_2a", "woodland_3", 30),
    ("woodland_3", "woodland_4", 30),
    ("woodland_4", "woodland_5", 15),
    ("woodland_4", "woodland_6", 30),
    ("woodland_5", "woodland_7", 30),
    ("woodland_6", "woodland_7", 15),
    ("woodland_6", "woodland_8", 30),
    ("woodland_7", "woodland_8", 30),
    ("woodland_8", "woodland_lot", 60) 
]

def locations():
    locations = []
    for tuple in locations_timings:
        if tuple[0] not in locations:
            locations.append(tuple[0])
        if tuple[1] not in locations:
            locations.append(tuple[1])
    return sorted(locations)

def main():
    print(locations())

if __name__ == "__main__":
    main()