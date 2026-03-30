#!/usr/bin/env python3
"""Tests for AI Agent Builder"""
import unittest
import subprocess
import os

class TestAgentBuilder(unittest.TestCase):
    
    def test_builder_script_exists(self):
        self.assertTrue(os.path.exists('agent_builder.py'))
    
    def test_builder_runs(self):
        result = subprocess.run(['python3', 'agent_builder.py'],
                              capture_output=True, text=True, timeout=10)
        self.assertIn('Agent', result.stdout)

if __name__ == '__main__':
    unittest.main()
