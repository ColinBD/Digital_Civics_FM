#!/usr/bin/python

#call this file using python txt2wavEx.py -L licence.lic -V heather.voice speechEx.xml
# so use: python txt2wavEx.py -L licence.lic -V heather.voice tweets.xml

# Copyright (c) 2011 Cereproc Ltd.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

#
# This is a simple program to produce audio output using the CereVoice
# Engine API.
#      

#
# Standard imports
#
import os
import sys


# Add CereVoice Engine to the path
thePath = 'cerevoice_eng/pylib/'
#sdkdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
#engdir = os.path.join(sdkdir, 'cerevoice_eng', 'pylib')
#sys.path.append(engdir)
sys.path.append(thePath)

                         
#
# Cereproc imports
#
import cerevoice_eng

def main():
    from optparse import OptionParser

    # Default input/output directory
    cwd = os.getcwd()
    
    # Setup option parsing
    usage="usage: %prog [options] -L licensefile -V voicefile infile1 [infile2...]\nSynthesise an xml or text file to a wave file and transcription."
    parser = OptionParser(usage=usage)

    parser.add_option("-L", "--licensefile", dest="licensefile",
                      help="CereProc license file")
    parser.add_option("-V", "--voicefile", dest="voicefile",
                      help="Voice file")
    parser.add_option("-o", "--outdir", dest="outdir", default=cwd,
                      help="Output directory, defaults to '%s'" % cwd)
    parser.add_option("-d", "--ondisk", dest="ondisk", action="store_true",
                      default=False, help="Load keeping audio and index data on disk")
    
    opts, args = parser.parse_args()

    # Check correct info supplied
    if len(args) < 1:
        parser.error("at least one input file must be supplied")
    if not opts.voicefile:
        parser.error("a voice file must be supplied")
    if not os.access(opts.voicefile, os.R_OK):
        parser.error("can't access voice file '%s'" % voicefile)
    if not os.access(opts.licensefile, os.R_OK):
        parser.error("can't access license file '%s'" % licensefile)
    if opts.outdir:
        if not os.access(opts.outdir, os.W_OK):
            parse.error("can't write to output directory output directory '%s'", opts.outdir)

    # Create an engine
    engine = cerevoice_eng.CPRCEN_engine_new()

    # Set the loading mode - all data to RAM or with audio and indexes on disk
    loadmode = cerevoice_eng.CPRC_VOICE_LOAD
    if opts.ondisk:
        loadmode = cerevoice_eng.CPRC_VOICE_LOAD_EMB

    # Load the voice
    ret = cerevoice_eng.CPRCEN_engine_load_voice(engine, opts.licensefile, "", opts.voicefile, loadmode)
    if not ret:
        sys.stderr.write("ERROR: could not load the voice, check license integrity\n")
        sys.exit(1)
    # Get some information about the first loaded voice (index 0)
    name = cerevoice_eng.CPRCEN_engine_get_voice_info(engine, 0, "VOICE_NAME");
    srate = cerevoice_eng.CPRCEN_engine_get_voice_info(engine, 0, "SAMPLE_RATE");
    sys.stderr.write("INFO: voice name is '%s', sample rate '%s'\n" % (name, srate))

    # Process the input files
    for f in args:
        indata = open(f).read()
        # Synthesise to a file
        wavout = os.path.join(opts.outdir, os.path.basename(os.path.splitext(f)[0])) + ".wav"
        cerevoice_eng.CPRCEN_engine_speak_to_file(engine, indata, wavout)
        sys.stderr.write("INFO: wrote wav file '%s'\n" % wavout)

    # Clean up
    cerevoice_eng.CPRCEN_engine_delete(engine)

if __name__ == '__main__':
    main()
