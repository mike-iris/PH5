# This file contains entry points and descriptions.
# To be used in setup.py, to define entry_points in the setup.
# Also provides a list of GUI and console apps when user types
# $ ph5

# Dave Thomas, 2019-08-06

PROG_VERSION = '2019.218'


class EntryPointTypes():
    GUI = "GUI Commands"
    CLIENT = "Extraction Clients"
    QC = "Quality Control"
    INGESTION = "Data and Metadata Ingestion"
    EDITING = "Editing and Manipulation"
    ALL = "Additional Commands"


class EntryPoint():

    def __init__(self, command, entry_point, description, type=None):
        self.command = command
        self.entry_point = entry_point
        self.description = description
        self.type = type

    def get_entry_point_str(self):
        return "{} = {}".format(self.command,
                                self.entry_point)

    def get_description_str(self):
        return "    {:30s} |    {}".format(self.command,
                                           self.description)


class CommandList():

    def __init__(self):
        self.entrypoints = {
            'gui_scripts': [
                EntryPoint('experiment_t_gen',
                           'ph5.utilities.changes:startapp',
                           'A GUI for building the experiment summary '
                           'kitchen-exchange format (kef) file.',
                           type=EntryPointTypes.GUI),
                EntryPoint('kefedit',
                           'ph5.utilities.kefedit:startapp',
                           'A GUI for opening, editing, and saving .kef '
                           'and .ph5 files.',
                           type=EntryPointTypes.ALL),
                EntryPoint('noven',
                           'ph5.utilities.noven:startapp',
                           'A GUI for converting CSV metatdata files into '
                           'kef files for PH5.',
                           type=EntryPointTypes.GUI),
                EntryPoint('pforma',
                           'ph5.utilities.pformagui:startapp',
                           'A GUI for loading MetaData into PH5.',
                           type=EntryPointTypes.GUI),
                ],
            'console_scripts': [
                EntryPoint('ph5',
                           'ph5.help:main',
                           'Display lists of PH5 scripts and GUIs.'),
                EntryPoint('cross_check_event_array_data',
                           'ph5.utilities.cross_check_event_array_data:main',
                           'Cross check Event, Array, and Data.',
                           type=EntryPointTypes.ALL),
                EntryPoint('dumpsegd',
                           'ph5.utilities.dumpsegd:main',
                           'Dump header of a SEG-D file '
                           '(Fairfield Node or SmartSolo)',
                           type=EntryPointTypes.ALL),
                EntryPoint('dumpsac',
                           'ph5.utilities.dumpsac:main',
                           'Translate and dump a binary '
                           'SAC file to stdout.',
                           type=EntryPointTypes.ALL),
                EntryPoint('dumpsgy',
                           'ph5.utilities.dumpsgy:main',
                           'Translate and dump a binary '
                           'SEGY file to stdout.',
                           type=EntryPointTypes.ALL),
                EntryPoint('keftokml',
                           'ph5.utilities.kef2kml:main',
                           'Converts a kef file to kml format.',
                           type=EntryPointTypes.QC),
                EntryPoint('meta_data_gen',
                           'ph5.utilities.meta_data_gen:main',
                           'Write info about receivers, events, or data.',
                           type=EntryPointTypes.ALL),
                EntryPoint('ph5tokef',
                           'ph5.utilities.tabletokef:main',
                           'Dump a table to a kef file.',
                           type=EntryPointTypes.QC),
                EntryPoint('keftocsv',
                           'ph5.utilities.keftocsv:main',
                           'Converts a kef (Kitchen Exchange '
                           'File) file to csv.',
                           type=EntryPointTypes.QC),
                EntryPoint('csvtokef',
                           'ph5.utilities.csvtokef:main',
                           'Converts a csv generated by keftocsv '
                           'to a kef file.',
                           type=EntryPointTypes.QC),
                EntryPoint('create_ext',
                           'ph5.utilities.create_ext:main',
                           'Create external link to a minifile for a das.',
                           type=EntryPointTypes.EDITING),
                EntryPoint('ph5_total',
                           'ph5.utilities.ph5_total:main',
                           'Find total size of ph5 files in a directory.',
                           type=EntryPointTypes.ALL),
                EntryPoint('ph5_validate',
                           'ph5.utilities.ph5validate:main',
                           'Runs set of checks on PH5 archive.',
                           type=EntryPointTypes.QC),
                EntryPoint('tabletokef',
                           'ph5.utilities.tabletokef:main',
                           'Alias to ph5tokef. Dump a table to a kef file.',
                           type=EntryPointTypes.ALL),
                EntryPoint('initialize_ph5',
                           'ph5.utilities.initialize_ph5:main',
                           'Program to initialize PH5 file '
                           'at start of experiment.',
                           type=EntryPointTypes.INGESTION),
                EntryPoint('125atoph5',
                           'ph5.utilities.texan2ph5:main',
                           'Allows the user to add Texan '
                           'raw data to the PH5 file.',
                           type=EntryPointTypes.INGESTION),
                EntryPoint('130toph5',
                           'ph5.utilities.1302ph5:main',
                           'Converts a csv generated by '
                           'keftocsv to a kef file.',
                           type=EntryPointTypes.INGESTION),
                EntryPoint('ph5_merge_helper',
                           'ph5.utilities.ph5_merge_helper:main',
                           'Modify Index_t.kef and miniPH5_xxxxx.ph5 '
                           'file names so they can be merged.',
                           type=EntryPointTypes.ALL),
                EntryPoint('recreate_external_references',
                           'ph5.utilities.recreate_external_references:main',
                           'Rebuild external references under '
                           'Receivers_g from info in Index_t.',
                           type=EntryPointTypes.ALL),
                EntryPoint('reporttoph5',
                           'ph5.utilities.report2ph5:main',
                           'Load a report (pdf) into a ph5 file.',
                           type=EntryPointTypes.INGESTION),
                EntryPoint('resp_load',
                           'ph5.utilities.resp_load:main',
                           'Fixes n_i numbers in the arrays, creates '
                           'new array.kef files, loads RESP files '
                           'into PH5 and creates a new "response.kef" file.',
                           type=EntryPointTypes.INGESTION),
                EntryPoint('seg2toph5',
                           'ph5.utilities.seg2toph5:main',
                           'Read data in SEG-2 revision 1 '
                           '(StrataVisor) into ph5 format.',
                           type=EntryPointTypes.INGESTION),
                EntryPoint('segdtoph5',
                           'ph5.utilities.segd2ph5:main',
                           'Read a standard SEG-D file and '
                           'load it into a PH5 file."',
                           type=EntryPointTypes.INGESTION),
                EntryPoint('segytoph5',
                           'ph5.utilities.segy2ph5:main',
                           'Read a standard SEG-Y file and '
                           'load it into a PH5 file.',
                           type=EntryPointTypes.INGESTION),
                EntryPoint('geo_kef_gen',
                           'ph5.utilities.geod2kef:main',
                           'Read locations and calculate offsets from '
                           'events to receivers, makes kef file for ph5.',
                           type=EntryPointTypes.INGESTION),
                EntryPoint('graotoph5',
                           'ph5.utilities.grao2ph5:main',
                           'Load MSEED data into a family of ph5 '
                           'files. Can use web services.',
                           type=EntryPointTypes.ALL),
                EntryPoint('time_kef_gen',
                           'ph5.utilities.time_kef_gen:main',
                           'Generates kef file to populate '
                           'Time_t from SOH_A.',
                           type=EntryPointTypes.INGESTION),
                EntryPoint('keftoph5',
                           'ph5.utilities.kef2ph5:main',
                           'Update a ph5 file from a kef file.',
                           type=EntryPointTypes.INGESTION),
                EntryPoint('metadatatoph5',
                           'ph5.utilities.metadatatoph5:main',
                           'Load metadata into PH5.',
                           type=EntryPointTypes.ALL),
                EntryPoint('mstoph5',
                           'ph5.utilities.obspytoph5:main',
                           'Takes data files and converts to PH5.',
                           type=EntryPointTypes.INGESTION),
                EntryPoint('pformacl',
                           'ph5.utilities.pformacl:main',
                           'Create or open a project and process '
                           'raw data to PH5 in parallel.',
                           type=EntryPointTypes.ALL),
                EntryPoint('sort_kef_gen',
                           'ph5.utilities.sort_kef_gen:main',
                           'Generate a kef file to populate Sort_t.',
                           type=EntryPointTypes.INGESTION),
                EntryPoint('delete_table',
                           'ph5.utilities.nuke_table:main',
                           'Initialize a table in a ph5 file. Deletes all '
                           'existing contents.',
                           type=EntryPointTypes.EDITING),
                EntryPoint('nuke_table',
                           'ph5.utilities.nuke_table:main',
                           'Alias to delete_table. Initialize a table in a '
                           'ph5 file. Deletes all existing contents.',
                           type=EntryPointTypes.ALL),
                EntryPoint('fix_3chan_texan',
                           'ph5.utilities.fix_3chan_texan:main',
                           'For fixing 3-channel Texan data.',
                           type=EntryPointTypes.ALL),
                EntryPoint('fix_srm',
                           'ph5.utilities.fix_srm:main',
                           'For fixing sample_rate_multiplier_i=0 or missing.',
                           type=EntryPointTypes.ALL),
                EntryPoint('fix_das_t_order',
                           'ph5.utilities.fix_das_t_order:main',
                           'Reorder das_t according to channel_number_i and '
                           'time.',
                           type=EntryPointTypes.ALL),
                EntryPoint('index_offset_t',
                           'ph5.utilities.index_offset_t:main',
                           'Index offset table in ph5 file to speed '
                           'up execution of kernel searches.',
                           type=EntryPointTypes.ALL),
                EntryPoint('load_das_t',
                           'ph5.utilities.load_das_t:main',
                           'Load a batch of Das_t keffiles.',
                           type=EntryPointTypes.ALL),
                EntryPoint('unsimpleton',
                           'ph5.utilities.unsimpleton:main',
                           'A command line utility to link Fairfield '
                           'SEG-D file names that expose information '
                           'about the contents of the file.',
                           type=EntryPointTypes.EDITING),
                EntryPoint('set_deploy_pickup_times',
                           'ph5.utilities.set_deploy_pickup_times:main',
                           'Set deploy and pickup times in '
                           'an Array_t_xxx.kef file.',
                           type=EntryPointTypes.ALL),
                EntryPoint('set_n_i_response',
                           'ph5.utilities.set_n_i_response:main',
                           'Updating the response table references '
                           'for multiple instrument types.',
                           type=EntryPointTypes.ALL),
                EntryPoint('sort_array_t',
                           'ph5.utilities.sort_array_t:main',
                           'Sort an Array_t_xxx.kef file by '
                           'station ID, id_s.',
                           type=EntryPointTypes.ALL),
                EntryPoint('report_gen',
                           'ph5.utilities.report_gen:main',
                           'Generate data_description.txt '
                           'and/or data_request_key.txt.',
                           type=EntryPointTypes.ALL),
                EntryPoint('ph5toevt',
                           'ph5.clients.ph5toevt:main',
                           'Extract events from a ph5 archive, '
                           'generate SEG-Y gathers in event order.',
                           type=EntryPointTypes.CLIENT),
                EntryPoint('ph5toexml',
                           'ph5.clients.ph5toexml:main',
                           'Not available.',
                           type=EntryPointTypes.ALL),
                EntryPoint('ph5toms',
                           'ph5.clients.ph5toms:main',
                           'Return mseed or SAC from a PH5 file.',
                           type=EntryPointTypes.CLIENT),
                EntryPoint('ph5torec',
                           'ph5.clients.ph5torec:main',
                           'Generate SEG-Y gathers in receiver order.',
                           type=EntryPointTypes.CLIENT),
                EntryPoint('ph5tostationxml',
                           'ph5.clients.ph5tostationxml:main',
                           'Takes PH5 files and returns StationXML.',
                           type=EntryPointTypes.CLIENT),
                EntryPoint('ph5availability',
                           'ph5.clients.ph5availability:main',
                           'Takes PH5 files and returns time series '
                           'availability info.',
                           type=EntryPointTypes.CLIENT),
                ],


            }
