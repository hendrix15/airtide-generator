import os


class UCTSConfig:
    def __init__(self, run_id: str, config: dict) -> None:
        args = config.get("ucts", {})
        self.max_nodes = args["max_nodes"]
        self.max_iter = args["max_iter"]
        self.minx = args["coordinate_range"][0][0]
        self.maxx = args["coordinate_range"][0][1]
        self.miny = args["coordinate_range"][1][0]
        self.maxy = args["coordinate_range"][1][1]
        self.minz = args["coordinate_range"][2][0]
        self.maxz = args["coordinate_range"][2][1]
        self.minlen = args["len_range"][0]
        self.maxlen = args["len_range"][1]
        self.minarea = args["area_range"][0]
        self.maxarea = args["area_range"][1]
        self.save_valid_count = 0
        self.save_invalid_count = 0
        self.global_iteration = 0
        self.MASS_OUTPUT_ALL_THRESHOLD = args["MASS_OUTPUT_ALL_THRESHOLD"]
        self.OUTPUT_ALL_MAX = 10000
        self.MASS_OUTPUT_ALL_MAX = 10000

        self.LOGFOLDER = os.path.join("output/search/", run_id)
        self.ALLFOLDER = os.path.join(self.LOGFOLDER, "Reward_ALL_Result/")
        self.MASS_ALLFOLDER = os.path.join(self.LOGFOLDER, "MASS_ALL_Result/")
        self.DIVERSITY_FOLDER = os.path.join(self.LOGFOLDER, "DIVERSITY_result/")
        self.DIVERSITY_TOPO_FOLDER = os.path.join(
            self.LOGFOLDER, "DIVERSITY_TOPO_result/"
        )

        for folder in [
            self.LOGFOLDER,
            self.ALLFOLDER,
            self.MASS_ALLFOLDER,
            self.DIVERSITY_FOLDER,
            self.DIVERSITY_TOPO_FOLDER,
        ]:
            if not os.path.exists(folder):
                os.makedirs(folder)


class TrussEnvironmentConfig:
    def __init__(self, config: dict) -> None:
        args = config.get("truss_env", {})
        self.E = args["E"]
        self.pho = args["pho"]
        self.sigma_T = args["sigma_T"]
        self.sigma_C = args["sigma_C"]
        self.slenderness_ratio_T = args["slenderness_ratio_c"]
        self.slenderness_ratio_C = args["slenderness_ratio_t"]
        self.dislimit = args["dislimit"]
        self.max_len = 5.0
        self.min_len = 0.03
        self.use_self_weight = True
        self.use_dis_constraint = True
        self.use_stress_constraint = True
        self.use_buckle_constraint = True
        self.use_slenderness_constraint = True
        self.use_longer_constraint = True
        self.use_shorter_constraint = True
        self.use_cross_constraint = True