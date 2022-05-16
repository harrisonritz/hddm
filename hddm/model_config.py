from .simulators import boundary_functions as bf
from .simulators import drift_functions as df
import numpy as np

model_config = {
    "ddm_vanilla": {
        "doc": "Model used internally for simulation purposes. Do NOT use with the LAN extension.",
        "params": ["v", "a", "z", "t"],
        "params_trans": [0, 0, 1, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0],
        "param_bounds": [[-5.0, 0.1, 0.05, 0], [5.0, 5.0, 0.95, 3.0]],
        "boundary": bf.constant,
        "params_default": [0.0, 2.0, 0.5, 0],
        "hddm_include": ["z"],
        "choices": [0, 1],
        "slice_widths": {
            "v": 1.5,
            "v_std": 1,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
        },
    },
    "full_ddm_vanilla": {
        "doc": "Model used internally for simulation purposes. Do NOT use with the LAN extension.",
        "params": ["v", "a", "z", "t", "sz", "sv", "st"],
        "params_trans": [0, 0, 1, 0, 0, 0, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0, 0.1, 0.5, 0.1],
        "param_bounds": [
            [-5.0, 0.1, 0.3, 0.25, 0, 0, 0],
            [5.0, 5.0, 0.7, 2.25, 0.25, 4.0, 0.25],
        ],
        "boundary": bf.constant,
        "params_default": [0.0, 1.0, 0.5, 0.25, 0, 0, 0],
        "hddm_include": ["z", "st", "sv", "sz"],
        "choices": [0, 1],
        "slice_widths": {
            "v": 1.5,
            "v_std": 1,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
            "sz": 1.1,  # AF-TODO: Might be worth downregulating and adding _std widths
            "st": 0.1,
            "sv": 0.5,
        },
    },
    "ddm": {
        "doc": "Basic DDM. Meant for use with the LAN extension. \n"
        + "Note that the boundaries here are coded as -a, and a in line with all other models meant for the LAN extension. \n"
        + "To compare model fits between standard HDDM and HDDMnn when using the DDM model, multiply the boundary "
        + "(a) parameter by 2. \n"
        + "We recommend using standard HDDM if you are interested in the basic DDM, but you might want to "
        + "use this for testing.",
        "params": ["v", "a", "z", "t"],
        "params_trans": [0, 0, 1, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0],
        "param_bounds": [[-3.0, 0.3, 0.1, 1e-3], [3.0, 2.5, 0.9, 2.0]],
        "boundary": bf.constant,
        "params_default": [0.0, 1.0, 0.5, 1e-3],
        "hddm_include": ["z"],
        "choices": [-1, 1],
        "slice_widths": {
            "v": 1.5,
            "v_std": 1,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
        },
    },
    "angle": {
        "doc": "Model formulation is described in the documentation under LAN Extension.\n"
        + "Meant for use with the extension.",
        "params": ["v", "a", "z", "t", "theta"],
        "params_trans": [0, 0, 1, 0, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0, 1.0],
        "param_bounds": [[-3.0, 0.3, 0.1, 1e-3, -0.1], [3.0, 3.0, 0.9, 2.0, 1.3]],
        "boundary": bf.angle,
        "params_default": [0.0, 1.0, 0.5, 1e-3, 0.1],
        "hddm_include": ["z", "theta"],
        "choices": [-1, 1],
        "slice_widths": {
            "v": 1.5,
            "v_std": 1,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
            "theta": 0.1,
            "theta_std": 0.2,
        },
    },
    "weibull": {
        "doc": "Model formulation is described in the documentation under LAN Extension.\n"
        + "Meant for use with the extension.",
        "params": ["v", "a", "z", "t", "alpha", "beta"],
        "params_trans": [0, 0, 1, 0, 0, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0, 2.0, 2.0],
        "param_bounds": [
            [-2.5, 0.3, 0.2, 1e-3, 0.31, 0.31],
            [2.5, 2.5, 0.8, 2.0, 4.99, 6.99],
        ],
        "boundary": bf.weibull_cdf,
        "params_default": [0.0, 1.0, 0.5, 1e-3, 3.0, 3.0],
        "hddm_include": ["z", "alpha", "beta"],
        "choices": [-1, 1],
        "slice_widths": {
            "v": 1.5,
            "v_std": 1,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
            "alpha": 1.0,
            "alpha_std": 0.5,
            "beta": 1.0,
            "beta_std": 0.5,
        },
    },
    "levy": {
        "doc": "Model formulation is described in the documentation under LAN Extension.\n"
        + "Meant for use with the extension.",
        "params": ["v", "a", "z", "alpha", "t"],
        "params_trans": [0, 0, 1, 0, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0, 1.0],
        "param_bounds": [[-3.0, 0.3, 0.1, 1.0, 1e-3], [3.0, 2.0, 0.9, 2.0, 2]],
        "boundary": bf.constant,
        "params_default": [0.0, 1.0, 0.5, 1.5, 1e-3],
        "hddm_include": ["z", "alpha"],
        "choices": [-1, 1],
        "slice_widths": {
            "v": 1.5,
            "v_std": 1,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
            "alpha": 1.0,
            "alpha_std": 0.5,
        },
    },
    "full_ddm": {
        "doc": "Currently unavailable, for LANs after switch to pytorch. \n"
        + "Coming soon... Please use standard HDDM if you want to fit this model to your data.",
        "params": ["v", "a", "z", "t", "sz", "sv", "st"],
        "params_trans": [0, 0, 1, 0, 0, 0, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0, 0.1, 0.5, 0.1],
        "param_bounds": [
            [-3.0, 0.3, 0.3, 0.25, 1e-3, 1e-3, 1e-3],
            [3.0, 2.5, 0.7, 2.25, 0.2, 2.0, 0.25],
        ],
        "boundary": bf.constant,
        "params_default": [0.0, 1.0, 0.5, 0.25, 1e-3, 1e-3, 1e-3],
        "hddm_include": ["z", "st", "sv", "sz"],
        "choices": [-1, 1],
        "slice_widths": {
            "v": 1.5,
            "v_std": 1,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
            "sz": 1.1,  # AF-TODO: Might be worth downregulating and adding _std widths
            "st": 0.1,
            "sv": 0.5,
        },
    },
    "ornstein": {
        "doc": "Model formulation is described in the documentation under LAN Extension."
        + "Meant for use with the extension.",
        "params": ["v", "a", "z", "g", "t"],
        "params_trans": [0, 0, 1, 0, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0, 1.0],
        "param_bounds": [[-2.0, 0.3, 0.2, -1.0, 1e-3], [2.0, 2.0, 0.8, 1.0, 2]],
        "boundary": bf.constant,
        "params_default": [0.0, 1.0, 0.5, 0.0, 1e-3],
        "hddm_include": ["z", "g"],
        "choices": [-1, 1],
        "slice_widths": {
            "v": 1.5,
            "v_std": 0.1,
            "a": 1,
            "a_std": 0.1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
            "g": 0.1,
            "g_trans": 0.2,
            "g_std": 0.1,
        },
    },
    "ddm_sdv": {
        "doc": "Currently unavailable, for LANs after switch to pytorch. Coming soon..."
        + "Please use standard HDDM if you want to fit this model to your data.",
        "params": ["v", "a", "z", "t", "sv"],
        "params_trans": [0, 0, 1, 0, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0, 1.0],
        "param_bounds": [[-3.0, 0.3, 0.1, 1e-3, 1e-3], [3.0, 2.5, 0.9, 2.0, 2.5]],
        "boundary": bf.constant,
        "params_default": [0.0, 1.0, 0.5, 1e-3, 1e-3],
        "hddm_include": ["z", "sv"],
        "choices": [-1, 1],
        "slice_widths": {
            "v": 1.5,
            "v_std": 1,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
            "sv": 0.5,  # AF-TODO: Might be worth adding std ?
        },
    "gamma_drift": {
        "doc": "Meant for use with the LAN extension",
        "params": ["v", "a", "z", "t", "shape", "scale", "c"],
        "params_trans": [0, 0, 1, 0, 0, 0, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0, 2.0, 2.0, 1.5],
        "param_bounds": [[-3.0, 0.3, 0.1, 1e-3, 2.0, 0.01, -3.0], [3.0, 3.0, 0.9, 2.0, 10.0, 1.0, 3.0]],
        "boundary": bf.constant,
        "params_default": [0.0, 1.0, 0.5, 0.25, 5.0, 0.5, 1.0],
        "hddm_include": ["z", "shape", "scale", "c"],
        "choices":[-1, 1],
        "slice_widths": {
            "v": 1.5,
            "v_std": 1,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
            "shape": 1,
            "shape_std": 1,
            "scale": 1,
            "scale_std": 1,
            "c": 1,
            "c_std": 1
        }
    },
    "gamma_drift_angle": {
        "doc": "Meant for use with the LAN extension",
        "params": ["v", "a", "z", "t", "theta", "shape", "scale", "c"],
        "params_trans": [0, 0, 1, 0, 0, 0, 0, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0, 1.0, 2.0, 2.0, 1.5],
        "param_bounds": [[-3.0, 0.3, 0.1, 1e-3, -0.1, 2.0, 0.01, -3.0], [3.0, 3.0, 0.9, 2.0, 1.3, 10.0, 1.0, 3.0]],
        "boundary": bf.angle,
        "params_default": [0.0, 1.0, 0.5, 0.25, 0.0, 5.0, 0.5, 1.0],
        "hddm_include": ["z", "shape", "scale", "c", "theta"],
        "choices":[-1, 1],
        "slice_widths": {
            "v": 1.5,
            "v_std": 1,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
            "theta": 0.1,
            "theta_std": 0.2,
            "shape": 1,
            "shape_std": 1,
            "scale": 1,
            "scale_std": 1,
            "c": 1,
            "c_std": 1
        }
    },
    },
    "ddm_par2": {
        "doc": "Currently undocumented, in testing phase.",
        "params": ["vh", "vl1", "vl2", "a", "zh", "zl1", "zl2", "t"],
        "params_trans": [0, 0, 0, 0, 1, 1, 1, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, None, None, None, 1.0],
        "param_bounds": [
            [-2.5, -2.5, -2.5, 0.3, 0.2, 0.2, 0.2, 0.0],
            [2.5, 2.5, 2.5, 2.0, 0.8, 0.8, 0.8, 2.0],
        ],
        "boundary": bf.constant,
        "params_default": [0.0, 0.0, 0.0, 1.0, 0.5, 0.5, 0.5, 1.0],
        "hddm_include": ["vh", "vl1", "vl2", "a", "zh", "zl1", "zl2", "t"],
        "choices": [0, 1, 2, 3],
        "slice_widths": {
            "vh": 1.5,
            "vh_std": 0.5,
            "vl1": 1.5,
            "vl1_std": 0.5,
            "vl2": 1.5,
            "vl2_std": 0.5,
            "a": 1,
            "a_std": 1,
            "zh": 0.1,
            "zh_trans": 0.2,
            "zl1": 0.1,
            "zl1_trans": 0.2,
            "zl2": 0.1,
            "zl2_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
        },
    },
    "ddm_par2_no_bias": {
        "doc": "Currently undocumented, in testing phase.",
        "params": ["vh", "vl1", "vl2", "a", "t"],
        "param_bounds": [[-2.5, -2.5, -2.5, 0.3, 0.0], [2.5, 2.5, 2.5, 2.0, 2.0]],
        "params_trans": [0, 0, 0, 0, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, 1.0],
        "boundary": bf.constant,
        "params_default": [0.0, 0.0, 0.0, 1.0, 1.0],
        "hddm_include": ["vh", "vl1", "vl2", "a", "t"],
        "choices": [0, 1, 2, 3],
        "slice_widths": {
            "vh": 1.5,
            "vh_std": 0.5,
            "vl1": 1.5,
            "vl1_std": 0.5,
            "vl2": 1.5,
            "vl2_std": 0.5,
            "a": 1,
            "a_std": 1,
            "t": 0.01,
            "t_std": 0.15,
        },
    },
    "ddm_par2_angle_no_bias": {
        "doc": "Currently undocumented, in testing phase.",
        "params": ["vh", "vl1", "vl2", "a", "t", "theta"],
        "param_bounds": [
            [-2.5, -2.5, -2.5, 0.3, 0.0, -0.1],
            [2.5, 2.5, 2.5, 2.0, 2.0, 1.0],
        ],
        "params_trans": [0, 0, 0, 0, 0, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, 1.0, 1.0],
        "boundary": bf.angle,
        "boundary_multiplicative": False,
        "params_default": [0.0, 0.0, 0.0, 1.0, 1.0, 0.0],
        "hddm_include": ["vh", "vl1", "vl2", "a", "t", "theta"],
        "choices": [0, 1, 2, 3],
        "slice_widths": {
            "vh": 1.5,
            "vh_std": 0.5,
            "vl1": 1.5,
            "vl1_std": 0.5,
            "vl2": 1.5,
            "vl2_std": 0.5,
            "a": 1,
            "a_std": 1,
            "t": 0.01,
            "t_std": 0.15,
            "theta": 0.1,
            "theta_std": 0.2,
        },
    },
    "ddm_par2_weibull_no_bias": {
        "doc": "Currently undocumented, in testing phase.",
        "params": ["vh", "vl1", "vl2", "a", "t", "alpha", "beta"],
        "param_bounds": [
            [-2.5, -2.5, -2.5, 0.3, 0.0, 0.31, 0.31],
            [2.5, 2.5, 2.5, 2.0, 2.0, 4.99, 6.99],
        ],
        "params_trans": [0, 0, 0, 0, 0, 0, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, 1.0, 1.5, 1.5],
        "boundary": bf.weibull_cdf,
        "boundary_multiplicative": True,
        "params_default": [0.0, 0.0, 0.0, 1.0, 1.0, 2.5, 3.5],
        "hddm_include": ["vh", "vl1", "vl2", "a", "t", "alpha", "beta"],
        "choices": [0, 1, 2, 3],
        "slice_widths": {
            "vh": 1.5,
            "vh_std": 0.5,
            "vl1": 1.5,
            "vl1_std": 0.5,
            "vl2": 1.5,
            "vl2_std": 0.5,
            "a": 1,
            "a_std": 1,
            "t": 0.01,
            "t_std": 0.15,
            "theta": 0.1,
            "theta_std": 0.2,
            "alpha": 1.0,
            "alpha_std": 0.5,
            "beta": 1.0,
            "beta_std": 0.5,
        },
    },
    "ddm_seq2": {
        "doc": "Currently undocumented, in testing phase.",
        "params": ["vh", "vl1", "vl2", "a", "zh", "zl1", "zl2", "t"],
        "params_trans": [0, 0, 0, 0, 1, 1, 1, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, None, None, None, 1.0],
        "param_bounds": [
            [-2.5, -2.5, -2.5, 0.3, 0.2, 0.2, 0.2, 0.0],
            [2.5, 2.5, 2.5, 2.0, 0.8, 0.8, 0.8, 2.0],
        ],
        "boundary": bf.constant,
        "params_default": [0.0, 0.0, 0.0, 1.0, 0.5, 0.5, 0.5, 1.0],
        "hddm_include": ["vh", "vl1", "vl2", "a", "zh", "zl1", "zl2", "t"],
        "choices": [0, 1, 2, 3],
        "slice_widths": {
            "vh": 1.5,
            "vh_std": 0.5,
            "vl1": 1.5,
            "vl1_std": 0.5,
            "vl2": 1.5,
            "vl2_std": 0.5,
            "a": 1,
            "a_std": 1,
            "zh": 0.1,
            "zh_trans": 0.2,
            "zl1": 0.1,
            "zl1_trans": 0.2,
            "zl2": 0.1,
            "zl2_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
        },
    },
    "ddm_seq2_no_bias": {
        "doc": "Currently undocumented, in testing phase.",
        "params": ["vh", "vl1", "vl2", "a", "t"],
        "param_bounds": [[-2.5, -2.5, -2.5, 0.3, 0.0], [2.5, 2.5, 2.5, 2.0, 2.0]],
        "params_trans": [0, 0, 0, 0, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, 1.0],
        "boundary": bf.constant,
        "params_default": [0.0, 0.0, 0.0, 1.0, 1.0],
        "hddm_include": ["vh", "vl1", "vl2", "a", "t"],
        "choices": [0, 1, 2, 3],
        "slice_widths": {
            "vh": 1.5,
            "vh_std": 0.5,
            "vl1": 1.5,
            "vl1_std": 0.5,
            "vl2": 1.5,
            "vl2_std": 0.5,
            "a": 1,
            "a_std": 1,
            "t": 0.01,
            "t_std": 0.15,
        },
    },
    "ddm_seq2_angle_no_bias": {
        "doc": "Currently undocumented, in testing phase.",
        "params": ["vh", "vl1", "vl2", "a", "t", "theta"],
        "param_bounds": [
            [-2.5, -2.5, -2.5, 0.3, 0.0, -0.1],
            [2.5, 2.5, 2.5, 2.0, 2.0, 1.0],
        ],
        "params_trans": [0, 0, 0, 0, 0, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, 1.0, 1.0],
        "boundary": bf.angle,
        "boundary_multiplicative": False,
        "params_default": [0.0, 0.0, 0.0, 1.0, 1.0, 0.0],
        "hddm_include": ["vh", "vl1", "vl2", "a", "t", "theta"],
        "choices": [0, 1, 2, 3],
        "slice_widths": {
            "vh": 1.5,
            "vh_std": 0.5,
            "vl1": 1.5,
            "vl1_std": 0.5,
            "vl2": 1.5,
            "vl2_std": 0.5,
            "a": 1,
            "a_std": 1,
            "t": 0.01,
            "t_std": 0.15,
            "theta": 0.1,
            "theta_std": 0.2,
        },
    },
    "ddm_seq2_weibull_no_bias": {
        "doc": "Currently undocumented, in testing phase.",
        "params": ["vh", "vl1", "vl2", "a", "t", "alpha", "beta"],
        "param_bounds": [
            [-2.5, -2.5, -2.5, 0.3, 0.0, 0.31, 0.31],
            [2.5, 2.5, 2.5, 2.0, 2.0, 4.99, 6.99],
        ],
        "params_trans": [0, 0, 0, 0, 0, 0, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, 1.0, 1.5, 1.5],
        "boundary": bf.weibull_cdf,
        "boundary_multiplicative": True,
        "params_default": [0.0, 0.0, 0.0, 1.0, 1.0, 2.5, 3.5],
        "hddm_include": ["vh", "vl1", "vl2", "a", "t", "alpha", "beta"],
        "choices": [0, 1, 2, 3],
        "slice_widths": {
            "vh": 1.5,
            "vh_std": 0.5,
            "vl1": 1.5,
            "vl1_std": 0.5,
            "vl2": 1.5,
            "vl2_std": 0.5,
            "a": 1,
            "a_std": 1,
            "t": 0.01,
            "t_std": 0.15,
            "alpha": 1.0,
            "alpha_std": 0.5,
            "beta": 1.0,
            "beta_std": 0.5,
        },
    },
    "ddm_mic2_adj": {
        "doc": "Currently undocumented, in testing phase.",
        "params": ["vh", "vl1", "vl2", "a", "zh", "zl1", "zl2", "d", "t"],
        "params_trans": [0, 0, 0, 0, 1, 1, 1, 1, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, None, None, None, None, 1.0],
        "param_bounds": [
            [-2.5, -2.5, -2.5, 0.3, 0.2, 0.2, 0.2, 0.0, 0.0],
            [2.5, 2.5, 2.5, 2.0, 0.8, 0.8, 0.8, 1.0, 2.0],
        ],
        "boundary": bf.constant,
        "params_default": [0.0, 0.0, 0.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.5],
        "hddm_include": ["vh", "vl1", "vl2", "a", "zh", "zl1", "zl2", "d", "t"],
        "choices": [0, 1, 2, 3],
        "slice_widths": {
            "vh": 1.5,
            "vh_std": 0.5,
            "vl1": 1.5,
            "vl1_std": 0.5,
            "vl2": 1.5,
            "vl2_std": 0.5,
            "a": 1,
            "a_std": 1,
            "zh": 0.1,
            "zh_trans": 0.2,
            "zl1": 0.1,
            "zl1_trans": 0.2,
            "zl2": 0.1,
            "zl2_trans": 0.2,
            "d": 0.1,
            "d_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
        },
    },
    "ddm_mic2_adj_no_bias": {
        "doc": "Currently undocumented, in testing phase.",
        "params": ["vh", "vl1", "vl2", "a", "d", "t"],
        "param_bounds": [
            [-2.5, -2.5, -2.5, 0.3, 0.0, 0.0],
            [2.5, 2.5, 2.5, 2.0, 1.0, 2.0],
        ],
        "params_trans": [0, 0, 0, 0, 0, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, 1.0, 1.0],
        "boundary": bf.constant,
        "params_default": [0.0, 0.0, 0.0, 1.0, 0.5, 1.0],
        "hddm_include": ["vh", "vl1", "vl2", "a", "d", "t"],
        "choices": [0, 1, 2, 3],
        "slice_widths": {
            "vh": 1.5,
            "vh_std": 0.5,
            "vl1": 1.5,
            "vl1_std": 0.5,
            "vl2": 1.5,
            "vl2_std": 0.5,
            "a": 1,
            "a_std": 1,
            "d": 0.1,
            "d_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
        },
    },
    "ddm_mic2_adj_angle_no_bias": {
        "doc": "Currently undocumented, in testing phase.",
        "params": ["vh", "vl1", "vl2", "a", "d", "t", "theta"],
        "param_bounds": [
            [-2.5, -2.5, -2.5, 0.3, 0.0, 0.0, -0.1],
            [2.5, 2.5, 2.5, 2.0, 1.0, 2.0, 1.0],
        ],
        "params_trans": [0, 0, 0, 0, 0, 0, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, 1.0, 1.0, 1.0],
        "boundary": bf.angle,
        "boundary_multiplicative": False,
        "params_default": [0.0, 0.0, 0.0, 1.0, 0.5, 1.0, 0.0],
        "hddm_include": ["vh", "vl1", "vl2", "a", "d", "t", "theta"],
        "choices": [0, 1, 2, 3],
        "slice_widths": {
            "vh": 1.5,
            "vh_std": 0.5,
            "vl1": 1.5,
            "vl1_std": 0.5,
            "vl2": 1.5,
            "vl2_std": 0.5,
            "a": 1,
            "a_std": 1,
            "d": 0.1,
            "d_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
            "theta": 0.1,
            "theta_std": 0.2,
        },
    },
    "ddm_mic2_adj_weibull_no_bias": {
        "doc": "Currently undocumented, in testing phase.",
        "params": ["vh", "vl1", "vl2", "a", "d", "t", "alpha", "beta"],
        "param_bounds": [
            [-2.5, -2.5, -2.5, 0.3, 0.0, 0.0, 0.31, 0.31],
            [2.5, 2.5, 2.5, 2.0, 1.0, 2.0, 4.99, 6.99],
        ],
        "params_trans": [0, 0, 0, 0, 0, 0, 0, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, 1.0, 1.0, 1.5, 1.5],
        "boundary": bf.weibull_cdf,
        "boundary_multiplicative": True,
        "params_default": [0.0, 0.0, 0.0, 1.0, 0.5, 1.0, 2.5, 3.5],
        "hddm_include": ["vh", "vl1", "vl2", "a", "d", "t", "alpha", "beta"],
        "choices": [0, 1, 2, 3],
        "slice_widths": {
            "vh": 1.5,
            "vh_std": 0.5,
            "vl1": 1.5,
            "vl1_std": 0.5,
            "vl2": 1.5,
            "vl2_std": 0.5,
            "a": 1,
            "a_std": 1,
            "d": 0.1,
            "d_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
            "alpha": 1.0,
            "alpha_std": 0.5,
            "beta": 1.0,
            "beta_std": 0.5,
        },
    },
    "race_no_bias_3": {
        "doc": "To be used with the LAN extension. Note, we suggest to fix z instead here, since it is essentially \n"
        + "redundant with the boundary separation parameter a. Future versions will drop z altogether.",
        "params": ["v0", "v1", "v2", "a", "z", "t"],
        "params_trans": [0, 0, 0, 0, 1, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, None, 1.0],
        "param_bounds": [
            [0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
            [2.5, 2.5, 2.5, 3.0, 0.9, 2.0],
        ],
        "boundary": bf.constant,
        "params_default": [0.0, 0.0, 0.0, 2.0, 0.5, 1e-3],
        "hddm_include": ["v0", "v1", "v2", "a", "z", "t"],
        "choices": [0, 1, 2],
        "slice_widths": {
            "v0": 1.5,
            "v0_std": 0.5,
            "v1": 1.5,
            "v1_std": 0.5,
            "v2": 1.5,
            "v2_std": 0.5,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
        },
    },
    "race_no_bias_angle_3": {
        "doc": "To be used with the LAN extension. Note, we suggest to fix z instead here, since it is essentially \n"
        + "redundant with the boundary separation parameter a. Future versions will drop z altogether.",
        "params": ["v0", "v1", "v2", "a", "z", "t", "theta"],
        "param_bounds": [
            [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.1],
            [2.5, 2.5, 2.5, 3.0, 0.9, 2.0, 1.45],
        ],
        "params_trans": [0, 0, 0, 0, 1, 0, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, None, 1.0, 1.0],
        "boundary": bf.angle,
        "params_default": [0.0, 0.0, 0.0, 2.0, 0.5, 1e-3, 0.0],
        "hddm_include": ["v0", "v1", "v2", "a", "z", "t", "theta"],
        "choices": [0, 1, 2],
        "slice_widths": {
            "v0": 1.5,
            "v0_std": 0.5,
            "v1": 1.5,
            "v1_std": 0.5,
            "v2": 1.5,
            "v2_std": 0.5,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
            "theta": 0.1,
            "theta_std": 0.2,
        },
    },
    "race_no_bias_4": {
        "doc": "To be used with the LAN extension. Note, we suggest to fix z instead here, since it is essentially \n"
        + "redundant with the boundary separation parameter a. Future versions will drop z altogether.",
        "params": ["v0", "v1", "v2", "v3", "a", "z", "t"],
        "param_bounds": [
            [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0],
            [2.5, 2.5, 2.5, 2.5, 3.0, 0.9, 2.0],
        ],
        "params_std_upper": [1.5, 1.5, 1.5, 1.5, 1.0, None, 1.0],
        "params_trans": [0, 0, 0, 0, 0, 1, 0],
        "boundary": bf.constant,
        "params_default": [0.0, 0.0, 0.0, 0.0, 2.0, 0.5, 1e-3],
        "hddm_include": ["v0", "v1", "v2", "v3", "a", "z", "t"],
        "choices": [0, 1, 2, 3],
        "slice_widths": {
            "v0": 1.5,
            "v0_std": 0.5,
            "v1": 1.5,
            "v1_std": 0.5,
            "v2": 1.5,
            "v2_std": 0.5,
            "v3": 1.5,
            "v3_std": 0.5,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
        },
    },
    "race_no_bias_angle_4": {
        "doc": "To be used with the LAN extension. Note, we suggest to fix z instead here, since it is essentially \n"
        + "redundant with the boundary separation parameter a. Future versions will drop z altogether.",
        "params": ["v0", "v1", "v2", "v3", "a", "z", "t", "theta"],
        "param_bounds": [
            [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, -0.1],
            [2.5, 2.5, 2.5, 2.5, 3.0, 0.9, 2.0, 1.45],
        ],
        "params_trans": [0, 0, 0, 0, 0, 1, 0, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.5, 1.0, None, 1.0, 1.0],
        "boundary": bf.angle,
        "params_default": [0.0, 0.0, 0.0, 0.0, 2.0, 0.5, 1e-3, 0.0],
        "hddm_include": ["v0", "v1", "v2", "v3", "a", "z", "t", "theta"],
        "choices": [0, 1, 2, 3],
        "slice_widths": {
            "v0": 1.5,
            "v0_std": 0.5,
            "v1": 1.5,
            "v1_std": 0.5,
            "v2": 1.5,
            "v2_std": 0.5,
            "v3": 1.5,
            "v3_std": 0.5,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
            "theta": 0.1,
            "theta_std": 0.2,
        },
    },
    "lca_no_bias_3": {
        "doc": "To be used with the LAN extension. Note, we suggest to fix z instead here, since it is essentially \n"
        + "redundant with the boundary separation parameter a. Future versions will drop z altogether.",
        "params": ["v0", "v1", "v2", "a", "z", "g", "b", "t"],
        "param_bounds": [
            [0.0, 0.0, 0.0, 1.0, 0.0, -1.0, -1.0, 0.0],
            [2.5, 2.5, 2.5, 3.0, 0.9, 1.0, 1.0, 2.0],
        ],
        "params_trans": [0, 0, 0, 0, 1, 0, 0, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, None, 1.0, 1.0, 1.0],
        "boundary": bf.constant,
        "params_default": [0.0, 0.0, 0.0, 2.0, 0.5, 0.0, 0.0, 1e-3],
        "hddm_include": ["v0", "v1", "v2", "a", "z", "g", "b", "t"],
        "choices": [0, 1, 2],
        "slice_widths": {
            "v0": 1.5,
            "v0_std": 0.5,
            "v1": 1.5,
            "v1_std": 0.5,
            "v2": 1.5,
            "v2_std": 0.5,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
            "g": 0.1,
            "g_std": 0.2,
            "b": 0.1,
            "b_std": 0.2,
        },
    },
    "lca_no_bias_angle_3": {
        "doc": "To be used with the LAN extension. Note, we suggest to fix z instead here, since it is essentially \n"
        + "redundant with the boundary separation parameter a. Future versions will drop z altogether.",
        "params": ["v0", "v1", "v2", "a", "z", "g", "b", "t", "theta"],
        "param_bounds": [
            [0.0, 0.0, 0.0, 1.0, 0.0, -1.0, -1.0, 0.0, -1.0],
            [2.5, 2.5, 2.5, 3.0, 0.9, 1.0, 1.0, 2.0, 1.45],
        ],
        "params_trans": [0, 0, 0, 0, 1, 0, 0, 0, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, None, 1.5, 1.0, 1.0, 1.0],
        "boundary": bf.angle,
        "params_default": [0.0, 0.0, 0.0, 2.0, 0.5, 0.0, 0.0, 1e-3, 0.0],
        "hddm_include": ["v0", "v1", "v2", "a", "z", "g", "b", "t", "theta"],
        "choices": [0, 1, 2],
        "slice_widths": {
            "v0": 1.5,
            "v0_std": 0.5,
            "v1": 1.5,
            "v1_std": 0.5,
            "v2": 1.5,
            "v2_std": 0.5,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
            "g": 0.1,
            "g_std": 0.2,
            "b": 0.1,
            "b_std": 0.2,
            "theta": 0.1,
            "theta_std": 0.2,
        },
    },
    "lca_no_bias_4": {
        "doc": "To be used with the LAN extension. Note, we suggest to fix z instead here, since it is essentially \n"
        + "redundant with the boundary separation parameter a. Future versions will drop z altogether.",
        "params": ["v0", "v1", "v2", "v3", "a", "z", "g", "b", "t"],
        "param_bounds": [
            [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, -1.0, -1.0, 0.0],
            [2.5, 2.5, 2.5, 2.5, 3.0, 0.9, 1.0, 1.0, 2.0],
        ],
        "params_trans": [0, 0, 0, 0, 0, 1, 0, 0, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.5, 1.0, None, 1.5, 1.0, 1.0],
        "boundary": bf.constant,
        "params_default": [0.0, 0.0, 0.0, 0.0, 2.0, 0.5, 0.0, 0.0, 1e-3],
        "hddm_include": ["v0", "v1", "v2", "v3", "a", "z", "g", "b", "t"],
        "choices": [0, 1, 2, 3],
        "slice_widths": {
            "v0": 1.5,
            "v0_std": 0.5,
            "v1": 1.5,
            "v1_std": 0.5,
            "v2": 1.5,
            "v2_std": 0.5,
            "v3": 1.5,
            "v3_std": 0.5,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
            "g": 0.1,
            "g_std": 0.2,
            "b": 0.1,
            "b_std": 0.2,
        },
    },
    "lca_no_bias_angle_4": {
        "doc": "To be used with the LAN extension. Note, we suggest to fix z instead here, since it is essentially \n"
        + "redundant with the boundary separation parameter a. Future versions will drop z altogether.",
        "params": ["v0", "v1", "v2", "v3", "a", "z", "g", "b", "t", "theta"],
        "param_bounds": [
            [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, -1.0, -1.0, 0.0, -0.1],
            [2.5, 2.5, 2.5, 2.5, 3.0, 0.9, 1.0, 1.0, 2.0, 1.45],
        ],
        "params_trans": [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.5, 1.0, None, 1.5, 1.0, 1.0, 1.0],
        "boundary": bf.angle,
        "params_default": [0.0, 0.0, 0.0, 0.0, 2.0, 0.5, 0.0, 0.0, 1e-3, 0.0],
        "hddm_include": ["v0", "v1", "v2", "v3", "a", "z", "g", "b", "t", "theta"],
        "choices": [0, 1, 2, 3],
        "slice_widths": {
            "v0": 1.5,
            "v0_std": 0.5,
            "v1": 1.5,
            "v1_std": 0.5,
            "v2": 1.5,
            "v2_std": 0.5,
            "v3": 1.5,
            "v3_std": 0.5,
            "a": 1,
            "a_std": 1,
            "z": 0.1,
            "z_trans": 0.2,
            "t": 0.01,
            "t_std": 0.15,
            "g": 0.1,
            "g_std": 0.2,
            "b": 0.1,
            "b_std": 0.2,
            "theta": 0.1,
            "theta_std": 0.2,
        },
    },
}

# Models for which configs can be reused
model_config["weibull_cdf"] = model_config["weibull"].copy()
model_config["full_ddm2"] = model_config["full_ddm"].copy()
